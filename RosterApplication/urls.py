from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
# ... other imports ...

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include([
        path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    ])),
    # ... your other URL patterns ...
] 