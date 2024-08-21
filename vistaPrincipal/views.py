from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import tema, articulo, busqueda

# Create your views here.

def vistaPrin(request):
    listaTemas = tema.objects.all().order_by('id')
    return render (request, 'vistaPrin.html',{
        'listaTemas':listaTemas 
    })

def nuevoTema(request):
    listaTemas = tema.objects.all().order_by('id')
    if request.method == 'POST':
        nombreTema = request.POST.get('nombreTema')
        descripcionTema = request.POST.get('descripcionTema')
        objTema = tema.objects.create(
            nombreTema=nombreTema,
            descripcionTema=descripcionTema,
        )
        objTema.save()
        return HttpResponseRedirect(reverse('vistaPrincipal:vistaPrin'))
    return render(request,'nuevoTema.html',{
        'listaTemas':listaTemas 
    })

def nuevoArticulo(request):
    listaTemas = tema.objects.all().order_by('id')
    if request.method =='POST':
        tituloArticulo =  request.POST.get('tituloArticulo')
        temaSeleccionado =  request.POST.get('temaSeleccionado')
        contenidoArticulo =  request.POST.get('contenidoArticulo')
        temaRelacionado = tema.objects.get(id=temaSeleccionado)
        objArticulo = articulo.objects.create(
            tituloArticulo=tituloArticulo,
            contenidoArticulo=contenidoArticulo,
            temaSeleccionado=temaRelacionado
        )
        objArticulo.save()
        return HttpResponseRedirect(reverse('vistaPrincipal:vistaPrin'))

    return render(request,'nuevoArticulo.html',{
        'listaTemas':listaTemas 
    })

def vistaArticulosPorTemas(request,idTema):
    listaTemas = tema.objects.all().order_by('id')
    objTema = tema.objects.get(id=idTema)
    listaArticulos = objTema.articulo_set.all()
    return render (request, 'vistaArticulosPorTemas.html',{
        'listaTemas':listaTemas,
        'objTema':objTema,
        'listaArticulos':listaArticulos,
    })

def vistaArticulo(request,idArticulo):
    listaTemas = tema.objects.all().order_by('id')
    objArticulo = articulo.objects.get(id=idArticulo)
    return render(request, 'vistaArticulo.html',{
         'listaTemas':listaTemas,
         'objArticulo':objArticulo,
    })

def vistaBusqueda(request):
    listaTemas = tema.objects.all().order_by('id')
    listaArticulos = articulo.objects.all().order_by('id')
    if request.method == 'POST':
        textoBusqueda = request.POST.get('textoBusqueda')
        listaArticulos = listaArticulos.filter(tituloArticulo__icontains=textoBusqueda)
        objBusqueda = busqueda.objects.create(
            textoBusqueda = textoBusqueda,
        )
        objBusqueda.save()
        return render(request, 'vistaBusqueda.html', {
            'listaTemas': listaTemas,
            'listaArticulos': listaArticulos,
            'textoBusqueda': textoBusqueda,
            'objBusqueda': objBusqueda,  
        })
    return render(request, 'vistaBusqueda.html',{
        'listaTemas':listaTemas,
        'listaArticulos':listaArticulos,
    })