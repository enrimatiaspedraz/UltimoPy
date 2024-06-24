from django.shortcuts import render, redirect
from .models import tablaProductos

# Create your views here.
def home(request): 
    productos = tablaProductos.objects.all()
    return render(request, 'gestionTablaProductos.html', {"productos":productos})

def base(request):
    return render(request, 'base.html')

def registrarPedido(request):
    codigo = request.POST['txtCodigo']
    producto = request.POST['txtProducto']
    cantidad = request.POST['numCantidad']
    
    pedido = tablaProductos.objects.create(
        Código=codigo, Producto=producto, Cantidad=cantidad)
    return redirect('/')

def editarPedido(request, codigo):
    pedido = tablaProductos.objects.get(Código=codigo)
    return render(request, 'edicionPedido.html', {"pedido":pedido})



def editarPedido2(request):
    codigo = request.POST['txtCodigo']
    producto = request.POST['txtProducto']
    cantidad = request.POST['numCantidad']
    
    pedido2 = tablaProductos.objects.get(Código=codigo)
    pedido2.Producto = producto
    pedido2.Cantidad = cantidad
    pedido2.save()
    
    return redirect('/')
    
   
 
def eliminarPedido(request, codigo):
    pedido = tablaProductos.objects.get(Código=codigo)
    pedido.delete()
    
    return redirect('/')
