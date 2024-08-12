from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.signin, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('detalles-ahorrar/', views.detalles_ahorrar, name='detalles_ahorrar'),
    path('detalles-inversion/', views.detalles_inversion,
         name='detalles_inversion'),
    path('detalles-deuda/', views.detalles_deuda, name='detalles_deuda'),
    path('detalles-planificacion/', views.detalles_planificacion,
         name='detalles_planificacion'),
    path('detalles-jubilacion/', views.detalles_jubilacion,
         name='detalles_jubilacion'),
    path('detalles-ahorro-inteligente/', views.detalles_ahorro_inteligente,
         name='detalles_ahorro_inteligente'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
