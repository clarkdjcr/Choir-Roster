from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, ChoirMemberForm
from django.contrib import messages
from users.models import ChoirMember
import logging
from django.conf import settings
import os

logger = logging.getLogger(__name__)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
        messages.error(request, 'Registration failed. Please check the form.')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def home(request):
    print("DEBUG: Home view called")
    print(f"DEBUG: Current directory: {os.getcwd()}")
    print(f"DEBUG: Template dirs: {settings.TEMPLATES[0]['DIRS']}")
    print(f"DEBUG: Looking for template at: {os.path.join(os.getcwd(), 'templates/users/home.html')}")
    
    if request.method == 'POST':
        form = ChoirMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ChoirMemberForm()
    
    choir_members = ChoirMember.objects.all().order_by('last_name')
    context = {
        'form': form,
        'choir_members': choir_members,
        'user': request.user
    }
    
    try:
        response = render(request, 'users/home.html', context)
        print(f"DEBUG: Response content length: {len(response.content)}")
        return response
    except Exception as e:
        print(f"DEBUG: Error rendering template: {str(e)}")
        raise