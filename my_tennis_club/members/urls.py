from django.urls import path
from . import views
from .views import CustomPasswordResetView

urlpatterns = [
    path('member/', views.members, name='members'),
    path('', views.index, name='index'),
    path('', views.home_view, name='home'),
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
    path('contact/', views.contact_view, name='contact'),
    path('news/', views.news_view, name='news'),
    path('list/', views.list_view, name='list'),
    path('login/', views.login_view, name='login'),
     path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),

]