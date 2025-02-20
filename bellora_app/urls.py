from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('proizvodi/', views.proizvodi, name='proizvodi'),
    path('dodaj-u-kosaricu/<int:proizvod_id>/', views.dodaj_u_kosaricu, name='dodaj_u_kosaricu'),
    path('kosarica/', views.kosarica, name='kosarica'),
]
