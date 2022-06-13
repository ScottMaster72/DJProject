from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Inicio, name='Inicio'),
    path('Nosotros', views.Nosotros, name='Nosotros'),
    path('Articulos', views.Articulos, name='Articulos'),
    path('Articulos/Crear', views.Crear, name='Crear'),
    path('Articulos/Editar', views.Editar, name='Editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('Articulos/Editar/<int:id>', views.Editar, name='Editar'),
    path('Sesion/Registro', views.FormRegistro, name='Registro'),
    path('Sesion/Cuenta', views.Cuenta, name='Cuenta'),
    path('Sesion/Editar', views.Editar_Sesion, name='Editar_Sesion'),
    path('Borrar/<int:Id>', views.Borrar, name='Borrar'),
    path('Sesion/Editar/<int:Id>', views.Editar_Sesion, name='Editar_Sesion'),
    path('proovedores', views.proovedores, name='proovedores'),
    path('Consola/indexC', views.consola, name='consola'),
    path('Promociones/indexP', views.promociones, name='promociones'),
    path('Merma/indexM', views.merma, name='merma'),
    path('Pedido/indice', views.pedido, name='pedido'),
    path('Pedido/CrearP', views.crearp, name='crearp'),
    path('Pedido/EditarP', views.editarp, name='editarp'),
    path('Pedido/EditarP/<int:Id>', views.editarp, name='editarp'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)