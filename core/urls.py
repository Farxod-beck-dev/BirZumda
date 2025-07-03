from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView,
    OrderListCreateView,
    OfferListCreateView,
    CategoryListView,
    ProfileUpdateView,
    UserDetailView,
    ChangePasswordView,
    LogoutView,
)

from .views import MyOrdersView, MyOffersView

from .views import OffersByOrderView

from .views import AcceptOfferView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('offers/', OfferListCreateView.as_view(), name='offer-list-create'),

    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),

    path('me/', UserDetailView.as_view(), name='user-detail'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('my-orders/', MyOrdersView.as_view(), name='my-orders'),
    path('my-offers/', MyOffersView.as_view(), name='my-offers'),

    path('orders/<int:order_id>/offers/', OffersByOrderView.as_view(), name='offers-by-order'),

    path('offers/<int:offer_id>/accept/', AcceptOfferView.as_view(), name='accept-offer'),

]
