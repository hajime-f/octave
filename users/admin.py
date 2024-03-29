from .models import User
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class AdminUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('last_name', 'first_name', 'last_name_kana', 'first_name_kana', 'old_last_name', 'old_last_name_kana', 'sex', 'birthday', 'postal_code', 'prefecture', 'address', 'building', 'tel', 'url', 'photo')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    list_display = ('get_full_name', 'get_full_name_kana', 'email', 'sex', 'birthday', 'postal_code', 'prefecture', 'address', 'building', 'tel', 'is_staff',)
    search_fields = ('username', 'email',)
    ordering = ('created_at',)
    filter_horizontal = ('groups', 'user_permissions',)
