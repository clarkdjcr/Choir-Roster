from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, ChoirMemberForm
from django.contrib import messages
from users.models import ChoirMember

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
    if request.method == 'POST':
        form = ChoirMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ChoirMemberForm()
    
    choir_members = ChoirMember.objects.all().order_by('last_name')
    return render(request, 'home.html', {
        'form': form,
        'choir_members': choir_members
    }) 