from django.shortcuts import render, redirect, get_object_or_404
from .models import Publicacion, Categoria, Comentario
from .forms import FormularioPublicacion, FormularioCategoria, FormularioComentario

def inicio(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'home.html', {'publicaciones': publicaciones})

def crear_post(request):
    if request.method == 'POST':
        formulario = FormularioPublicacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario = FormularioPublicacion()
    return render(request, 'crear_post.html', {'formulario': formulario})

def crear_categoria(request):
    if request.method == 'POST':
        formulario = FormularioCategoria(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario = FormularioCategoria()
    return render(request, 'crear_categoria.html', {'formulario': formulario})

def crear_comentario(request, post_id):
    publicacion = get_object_or_404(Publicacion, id=post_id)
    if request.method == 'POST':
        formulario = FormularioComentario(request.POST)
        if formulario.is_valid():
            comentario = formulario.save(commit=False)
            comentario.publicacion = publicacion
            comentario.save()
            return redirect('detalle_post', post_id=publicacion.id)
    else:
        formulario = FormularioComentario()
    return render(request, 'crear_comentario.html', {'formulario': formulario, 'publicacion': publicacion})

def buscar_publicaciones(request):
    query = request.GET.get('q', '')
    publicaciones = Publicacion.objects.filter(titulo__icontains=query)
    return render(request, 'resultados_busqueda.html', {'publicaciones': publicaciones, 'query': query})

def detalle_post(request, post_id):
    publicacion = get_object_or_404(Publicacion, id=post_id)
    comentarios = publicacion.comentarios.all()
    return render(request, 'detalle_post.html', {
        'publicacion': publicacion,
        'comentarios': comentarios,
    })
