from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear_post/', views.crear_post, name='crear_post'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear_comentario/<int:post_id>/', views.crear_comentario, name='crear_comentario'),
    path('buscar/', views.buscar_publicaciones, name='buscar_publicaciones'),
    path('post/<int:post_id>/', views.detalle_post, name='detalle_post'),
]
