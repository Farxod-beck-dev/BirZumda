from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Order, Offer, Category, Profile

User = get_user_model()

# ✅ Ro'yxatdan o'tish serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'name', 'password')

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data['name']
        )

# ✅ Buyurtma serializer
class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('customer', 'created_at')

# ✅ Taklif serializer
class OfferSerializer(serializers.ModelSerializer):
    provider = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Offer
        fields = '__all__'
        read_only_fields = ('provider', 'created_at')

# ✅ Kategoriya serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# ✅ Profil serializer (kategoriya tanlash uchun alohida id bilan)
class ProfileSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        write_only=True,
        source='categories'
    )

    class Meta:
        model = Profile
        fields = ['categories', 'category_ids', 'is_provider']
