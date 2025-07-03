from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions, filters, serializers
from rest_framework.generics import RetrieveUpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

from .models import Order, Offer, Category, Profile
from .serializers import (
    RegisterSerializer,
    OrderSerializer,
    OfferSerializer,
    CategorySerializer,
    ProfileSerializer
)

User = get_user_model()

# ✅ Ro‘yxatdan o‘tish
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Ro‘yxatdan o‘tildi!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Buyurtmalar ro‘yxati va yaratish
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    filterset_fields = ['created_at']
    ordering_fields = ['created_at']

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

# ✅ Faqat o‘zining buyurtmalari
class MyOrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)

# ✅ Takliflar ro‘yxati va yaratish
class OfferListCreateView(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        order = serializer.validated_data.get('order')

        if not user_profile.is_provider:
            raise serializers.ValidationError("Faqat ustalar (provider) taklif bera oladi.")

        if order.category not in user_profile.categories.all():
            raise serializers.ValidationError("Bu buyurtma sizning sohangizga mos emas.")

        serializer.save(provider=self.request.user)

# ✅ Faqat o‘zining takliflari
class MyOffersView(generics.ListAPIView):
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Offer.objects.filter(provider=self.request.user)

# ✅ Kategoriyalar ro‘yxati
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

# ✅ Profil yangilash
class ProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

# ✅ Foydalanuvchi ma’lumotlari
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'is_active', 'is_staff']
        read_only_fields = ['email']

class UserDetailView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

# ✅ Parolni yangilash
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not user.check_password(old_password):
            return Response({"detail": "Eski parol noto‘g‘ri."}, status=400)

        user.set_password(new_password)
        user.save()
        return Response({"detail": "Parol muvaffaqiyatli yangilandi."})

# ✅ Logout (Frontend tokenni o‘chiradi)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response({"detail": "Chiqildi (token frontenddan o‘chirilishi kerak)."})

# ✅ Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="BirZum API",
        default_version='v1',
        description="Ustalar va tadbirkorlar uchun raqamli platforma",
        contact=openapi.Contact(email="birzum@startup.uz"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# ✅ Muayyan buyurtmaga berilgan takliflar
class OffersByOrderView(generics.ListAPIView):
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        order_id = self.kwargs['order_id']
        return Offer.objects.filter(order_id=order_id)
class AcceptOfferView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, offer_id):
        try:
            offer = Offer.objects.get(id=offer_id)
        except Offer.DoesNotExist:
            return Response({"detail": "Taklif topilmadi."}, status=404)

        # Faqat buyurtma egasi tasdiqlashi mumkin
        if offer.order.customer != request.user:
            return Response({"detail": "Siz faqat o'zingizga tegishli taklifni qabul qila olasiz."}, status=403)

        # Avvalgi takliflarni bekor qilish
        Offer.objects.filter(order=offer.order).update(is_accepted=False)

        # Tanlangan taklifni tasdiqlash
        offer.is_accepted = True
        offer.save()

        return Response({"detail": "Taklif muvaffaqiyatli qabul qilindi."})
