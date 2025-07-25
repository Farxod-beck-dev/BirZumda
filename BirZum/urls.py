from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="BirZum API",
      default_version='v1',
      description="BirZum platformasi uchun API hujjati",
      contact=openapi.Contact(email="birzum@support.uz"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

# Swagger uchun
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="BirZum API",
      default_version='v1',
      description="Swagger hujjati",
      contact=openapi.Contact(email="you@example.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



schema_view = get_schema_view(
   openapi.Info(
      title="BirZum API",
      default_version='v1',
      description="Freelance xizmatlari uchun API hujjatlari",
      contact=openapi.Contact(email="support@birzum.uz"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),

    # JWT token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger & Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # <– sizning endpointlaringiz shu faylga boradi
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
