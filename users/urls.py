from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('add/', views.add_member, name='add_member'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('delete/<int:member_id>/', views.delete_member, name='delete_member'),
    path('edit/<int:member_id>/', views.edit_member, name='edit_member'),
]
