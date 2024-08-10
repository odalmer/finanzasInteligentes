from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('detalles-ahorrar/', views.detalles_ahorrar, name='detalles_ahorrar'),
    path('detalles-inversion/', views.detalles_inversion, name='detalles_inversion'),
    path('detalles-deuda/', views.detalles_deuda, name='detalles_deuda'),
    path('detalles-planificacion/', views.detalles_planificacion, name='detalles_planificacion'),
    path('detalles-jubilacion/', views.detalles_jubilacion, name='detalles_jubilacion'),
    path('detalles-ahorro-inteligente/', views.detalles_ahorro_inteligente, name='detalles_ahorro_inteligente'),
]
