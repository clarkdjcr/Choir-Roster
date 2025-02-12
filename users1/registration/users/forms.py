from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, ChoirMember

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class ChoirMemberForm(forms.ModelForm):
    class Meta:
        model = ChoirMember
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'voice_part', 'picture'] 