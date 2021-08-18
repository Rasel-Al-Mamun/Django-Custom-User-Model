from .models import User
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ('-date_joined',)
    list_display = ('email', 'is_active', 'is_admin', 'is_staff', 'is_superuser')
    list_filter = ('email', 'is_admin', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name',)}),
        (_('Permissions'), {
         'fields': ('is_active', 'is_admin', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
         }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    readonly_fields = ('id', 'date_joined', 'last_login')
    filter_horizontal = ('groups', 'user_permissions',)
