from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ChoirMemberForm
from django.contrib import messages
from .models import ChoirMember
import logging
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.middleware.csrf import get_token
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import views as auth_views

logger = logging.getLogger(__name__)

# Create a custom UserCreationForm for our CustomUser
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields

@csrf_protect
def register(request):
    """Handle new user and choir member registration"""
    try:
        if request.method == 'POST':
            print("POST data received")  # Debug print
            user_form = CustomUserCreationForm(request.POST)
            member_form = ChoirMemberForm(request.POST, request.FILES)
            
            if user_form.is_valid() and member_form.is_valid():
                print("Forms are valid")  # Debug print
                # Save the user first
                user = user_form.save()
                print(f"User saved: {user.username}")  # Debug print
                
                # Create the choir member and link to user
                member = member_form.save(commit=False)
                member.user = user
                member.save()
                print(f"Choir member saved: {member.first_name} {member.last_name}")  # Debug print
                
                # Log the user in
                login(request, user)
                return redirect('home')
            else:
                print("Form errors:")  # Debug print
                print("User form errors:", user_form.errors)
                print("Member form errors:", member_form.errors)
        else:
            user_form = CustomUserCreationForm()
            member_form = ChoirMemberForm()

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Register - DUMC Choir</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                <div class="container">
                    <a class="navbar-brand" href="/">DUMC Choir Roster</a>
                    <div class="navbar-nav ms-auto">
                        <a class="nav-link" href="/login/">Login</a>
                    </div>
                </div>
            </nav>

            <div class="container mt-5">
                <div class="row justify-content-center">
                    <div class="col-md-8">
                        <div class="card">
                            <div class="card-header">
                                <h2>Register New Choir Member</h2>
                            </div>
                            <div class="card-body">
                                <form method="post" enctype="multipart/form-data">
                                    <input type="hidden" name="csrfmiddlewaretoken" value="{get_token(request)}" />
                                    
                                    <h4 class="mb-3">Account Information</h4>
                                    <div class="mb-4">
                                        {str(user_form.as_p())}
                                    </div>
                                    
                                    <h4 class="mb-3">Choir Member Information</h4>
                                    <div class="mb-4">
                                        {str(member_form.as_p())}
                                    </div>
                                    
                                    <button type="submit" class="btn btn-primary">Register</button>
                                </form>
                                
                                <p class="mt-3">
                                    Already have an account? <a href="/login/">Login here</a>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
        return HttpResponse(html)

    except Exception as e:
        error_msg = f"Error: {str(e)}"
        print("Debug error:", error_msg)
        return HttpResponse(f"An error occurred: {str(e)}")

@login_required
def home(request):
    try:
        if not request.user.is_authenticated:
            # Show login/register page for non-authenticated users
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>DUMC Choir Roster - Welcome</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
            </head>
            <body>
                <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                    <div class="container">
                        <a class="navbar-brand" href="/">DUMC Choir Roster</a>
                        <div class="navbar-nav ms-auto">
                            <a class="nav-link" href="/login/">Login</a>
                            <a class="nav-link" href="/register/">Register</a>
                        </div>
                    </div>
                </nav>
                <div class="container mt-5">
                    <div class="jumbotron">
                        <h1>Welcome to DUMC Choir Roster</h1>
                        <p class="lead">Please login or register to access the choir roster.</p>
                    </div>
                </div>
            </body>
            </html>
            """
            return HttpResponse(html)

        # For authenticated users, show the roster
        choir_members = ChoirMember.objects.all().order_by('last_name', 'first_name')
        
        # Generate member cards HTML
        member_cards = ""
        for member in choir_members:
            member_cards += f"""
                <div class="col-md-4 mb-4">
                    <div class="card h-100">
                        {'<img src="' + member.picture.url + '" class="card-img-top" style="height: 200px; object-fit: cover;">' if member.picture else ''}
                        <div class="card-body">
                            <h5 class="card-title">{member.first_name} {member.last_name}</h5>
                            <p class="card-text">
                                <strong>Voice Part:</strong> {member.get_voice_part_display()}<br>
                                <strong>Phone:</strong> {member.phone_number}<br>
                                <strong>Address:</strong> {member.address}
                            </p>
                            <div class="btn-group">
                                <a href="/edit/{member.id}/" class="btn btn-primary btn-sm">Edit</a>
                                <button onclick="deleteMember({member.id})" class="btn btn-danger btn-sm">Delete</button>
                            </div>
                        </div>
                    </div>
                </div>
            """

        # Generate the complete page for authenticated users
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>DUMC Choir Roster</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
                .card-img-top {{
                    height: 200px;
                    object-fit: cover;
                }}
            </style>
        </head>
        <body>
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                <div class="container">
                    <a class="navbar-brand" href="/">DUMC Choir Roster</a>
                    <div class="navbar-nav ms-auto">
                        <a class="nav-link" href="#" onclick="logoutUser(); return false;">Logout</a>
                    </div>
                </div>
            </nav>

            <div class="container mt-4">
                <h2>Choir Members</h2>
                <div class="row">
                    {member_cards}
                </div>
            </div>

            <script>
                function deleteMember(id) {{
                    if (confirm('Are you sure you want to delete this member?')) {{
                        fetch(`/delete/${{id}}/`, {{
                            method: 'POST',
                            headers: {{
                                'X-CSRFToken': '{get_token(request)}'
                            }}
                        }}).then(() => window.location.reload());
                    }}
                }}
                
                function logoutUser() {{
                    if (confirm('Are you sure you want to logout?')) {{
                        fetch('/logout/', {{
                            method: 'POST',
                            headers: {{
                                'X-CSRFToken': '{get_token(request)}'
                            }}
                        }}).then(() => {{
                            window.location.href = '/';
                        }});
                    }}
                }}
            </script>
        </body>
        </html>
        """
        
        return HttpResponse(html)
        
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        print("Debug:", error_msg)
        return HttpResponse(error_msg)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponse('{"status": "success"}')
    return HttpResponse('{"status": "error", "message": "Method not allowed"}', status=405)

@login_required
def roster(request):
    choir_members = ChoirMember.objects.all().order_by('last_name')
    form = ChoirMemberForm()
    return render(request, 'users/roster.html', {
        'form': form,
        'choir_members': choir_members,
    })

@login_required
def add_member(request):
    if request.method == 'POST':
        form = ChoirMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Choir member added successfully!')
            return redirect('home')
    return redirect('home')

@login_required
def edit_member(request, member_id):
    try:
        member = ChoirMember.objects.get(id=member_id)
        
        if request.method == 'POST':
            form = ChoirMemberForm(request.POST, request.FILES, instance=member)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = ChoirMemberForm(instance=member)

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Edit Choir Member - DUMC Choir</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                <div class="container">
                    <a class="navbar-brand" href="/">DUMC Choir Roster</a>
                    <div class="navbar-nav ms-auto">
                        <a class="nav-link" href="/">Home</a>
                        <a class="nav-link" href="#" onclick="logoutUser(); return false;">Logout</a>
                    </div>
                </div>
            </nav>

            <div class="container mt-5">
                <div class="row justify-content-center">
                    <div class="col-md-8">
                        <div class="card">
                            <div class="card-header">
                                <h2>Edit Choir Member</h2>
                            </div>
                            <div class="card-body">
                                <form method="post" enctype="multipart/form-data">
                                    <input type="hidden" name="csrfmiddlewaretoken" value="{get_token(request)}" />
                                    {str(form.as_p())}
                                    <div class="mt-3">
                                        <button type="submit" class="btn btn-primary">Save Changes</button>
                                        <a href="/" class="btn btn-secondary">Cancel</a>
                                    </div>
                                </form>
                            </div>
                        </div>
                        
                        {f'<div class="card mt-3"><div class="card-body"><img src="{member.picture.url}" class="img-fluid" alt="Current photo"></div></div>' if member.picture else ''}
                    </div>
                </div>
            </div>

            <script>
                function logoutUser() {{
                    if (confirm('Are you sure you want to logout?')) {{
                        fetch('/logout/', {{
                            method: 'POST',
                            headers: {{
                                'X-CSRFToken': '{get_token(request)}'
                            }}
                        }}).then(() => {{
                            window.location.href = '/';
                        }});
                    }}
                }}
            </script>
        </body>
        </html>
        """
        return HttpResponse(html)

    except ChoirMember.DoesNotExist:
        return HttpResponse("Choir member not found", status=404)
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        print("Debug error:", error_msg)
        return HttpResponse(f"An error occurred: {str(e)}")

@login_required
def delete_member(request, member_id):
    member = get_object_or_404(ChoirMember, id=member_id)
    if request.method == 'POST':
        if member.picture:
            member.picture.delete()
        member.delete()
        messages.success(request, 'Choir member deleted successfully!')
    return redirect('home')

# Add this new class-based view
class CustomLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_password_reset'] = True
        return context 