from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User, Order, Offer, Category, Profile

class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'get_name', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('email',)
    search_fields = ('email', 'name')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_superuser')}
        ),
    )

    def get_name(self, obj):
        return obj.name
    get_name.short_description = 'Name'

# ✅ Avval ro‘yxatdan o‘tgan bo‘lsa, chiqaramiz
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

# ✅ Model registratsiyasi
admin.site.register(User, CustomUserAdmin)
admin.site.register(Order)
admin.site.register(Offer)
admin.site.register(Category)
admin.site.register(Profile)
