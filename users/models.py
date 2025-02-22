from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    VOICE_CHOICES = [
        ('S1', 'Soprano 1'),
        ('S2', 'Soprano 2'),
        ('A1', 'Alto 1'),
        ('A2', 'Alto 2'),
        ('T1', 'Tenor 1'),
        ('T2', 'Tenor 2'),
        ('B1', 'Bass 1'),
        ('B2', 'Bass 2'),
    ]
    
    # Personal and Contact Info
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    # Choir Info (combined with personal info)
    voice_part = models.CharField(max_length=2, choices=VOICE_CHOICES, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}" if self.first_name and self.last_name else self.username

    class Meta:
        ordering = ['first_name', 'last_name']

class ChoirMember(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    voice_part = models.CharField(max_length=2, choices=[
        ('S1', 'Soprano 1'),
        ('S2', 'Soprano 2'),
        ('A1', 'Alto 1'),
        ('A2', 'Alto 2'),
        ('T1', 'Tenor 1'),
        ('T2', 'Tenor 2'),
        ('B1', 'Bass 1'),
        ('B2', 'Bass 2'),
    ])
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    picture = models.ImageField(upload_to='choir_members/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name'] 