from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('base/', views.base),
    path('registrarPedido/', views.registrarPedido),
    path('editarPedido/<codigo>', views.editarPedido),
    path('editarPedido2/', views.editarPedido2),    
    path('eliminarPedido/<codigo>', views.eliminarPedido),
]