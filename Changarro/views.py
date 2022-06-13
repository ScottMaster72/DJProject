from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Articulo
from .models import Registro
from .models import Proovedores
from .models import Sucursales
from .models import Consola
from .models import Promociones
from .models import Merma
from .models import Pedido
from .Forms import ArticuloForm
from .Forms import RegistroForm
from .Forms import PedidoForm


# Create your views here.

def Inicio(request):
    return render(request, 'Inicio.html')


def Nosotros(request):
    sucursales = Sucursales.objects.all()
    return render(request, 'Nosotros.html', {'Sucursales':sucursales})


def Articulos(request):
    Articulos = Articulo.objects.all()
    return render(request, 'Articulos/Index.html', {'Articulos': Articulos})


def Crear(request):
    formulario = ArticuloForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('Articulos')
    return render(request, 'Articulos/Crear.html', {'formulario': formulario})


def Editar(request, id):
    articulo = Articulo.objects.get(id=id)
    formulario = ArticuloForm(request.POST or None, request.FILES or None, instance=articulo)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('Articulos')
    return render(request, 'Articulos/Editar.html', {'formulario': formulario})


def eliminar(request, id):
    articulo = Articulo.objects.get(id=id)
    articulo.delete()
    return redirect('Articulos')


def Cuenta(request):
    Registros = Registro.objects.all()
    return render(request, 'Sesion/Cuenta.html', {'Registro': Registros})


def FormRegistro(request):
    form = RegistroForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('Inicio')
    return render(request, 'Sesion/Registro.html', {'form': form})


def Borrar(request, Id):
    Registros = Registro.objects.get(id=Id)
    Registros.delete()
    return redirect('Cuenta')


def Editar_Sesion(request, Id):
    Registros = Registro.objects.get(id=Id)
    form = RegistroForm(request.POST or None, request.FILES or None, instance=Registros)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('Cuenta')
    return render(request, 'Sesion/Editar.html', {'form':form})


def proovedores(request):
    proovedores = Proovedores.objects.all()
    return render(request, 'Proovedores/index2.html', {'proovedores':proovedores})


def consola(request):
    consola = Consola.objects.all()
    return render(request, 'Consola/indexC.html', {'consola':consola})


def promociones(request):
    promociones = Promociones.objects.all()
    return render(request, 'Promociones/indexP.html', {'promociones':promociones})


def merma(request):
    merma = Merma.objects.all()
    return render(request, 'Merma/indexM.html', {'merma':merma})


def pedido(request):
    pedido = Pedido.objects.all()
    return render(request, 'Pedido/indice.html', {'pedido':pedido})


def crearp(request):
    formulario = PedidoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('pedido')
    return render(request, 'Pedido/CrearP.html', {'formulario':formulario})


def editarp(request, Id):
    pedido = Pedido.objects.get(Id=Id)
    formulario = PedidoForm(request.POST or None, request.FILES or None, instance=pedido)
    if formulario.is_valid():
        formulario.save()
        return redirect('pedido')
    return render(request, 'Pedido/EditarP.html', {'formulario':formulario})