from django.contrib import admin

from core.models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    exclude = ('password',)
    readonly_fields = ('date_joined', 'last_login',)
