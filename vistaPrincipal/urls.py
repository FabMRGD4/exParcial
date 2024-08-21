from django.urls import path, include
from . import views

app_name = 'vistaPrincipal'

urlpatterns = [
    path('', views.vistaPrin, name = 'vistaPrin'),
    path('nuevoTema', views.nuevoTema,name='nuevoTema'),
    path('nuevoArticulo', views.nuevoArticulo, name='nuevoArticulo'),
    path('vistaArticulosPorTemas/<str:idTema>',views.vistaArticulosPorTemas, name='vistaArticulosPorTemas'),
    path('vistaArticulo/<str:idArticulo>',views.vistaArticulo, name = 'vistaArticulo'),
    path('vistaBusqueda',views.vistaBusqueda, name='vistaBusqueda'),
]
