from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'voice_part', 'is_staff')
    list_filter = ('voice_part', 'is_staff', 'is_superuser')
    fieldsets = UserAdmin.fieldsets + (
        ('Choir Information', {'fields': ('phone_number', 'address', 'profile_picture', 'voice_part')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Choir Information', {'fields': ('phone_number', 'address', 'profile_picture', 'voice_part')}),
    )

admin.site.register(CustomUser, CustomUserAdmin) 