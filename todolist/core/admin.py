from django.contrib import admin

from core.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    exclude = ('password',)
    readonly_fields = ('date_joined', 'last_login',)
