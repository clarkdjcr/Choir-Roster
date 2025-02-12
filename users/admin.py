from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import ChoirMember

class ChoirMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'voice_part', 'phone_number')
    list_filter = ('voice_part',)
    search_fields = ('first_name', 'last_name', 'phone_number')
    ordering = ('last_name', 'first_name')

    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'phone_number', 'address')
        }),
        ('Choir Details', {
            'fields': ('voice_part', 'picture')
        }),
        ('Account Information', {
            'fields': ('user',)
        }),
    )

admin.site.register(ChoirMember, ChoirMemberAdmin) 