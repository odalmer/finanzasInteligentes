from django.urls import path, include
from . import views
from .views import CustomPasswordResetView
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('member/', views.members, name='members'),
    path('', views.index, name='index'),
    path('home', views.home_view, name='home'),
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
    path('contact/', views.contact_view, name='contact'),
    path('news/', views.news_view, name='news'),
    path('list/', views.list_view, name='list'),
    path('login/', views.login_view, name='login'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('profile/', views.profile_view, name='profile'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    

]