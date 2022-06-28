from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio , name="inicio"),
    path("profesores" , views.profesores , name="profesores"),
    path("cursos" , views.cursos , name="cursos"),
    path("alumnos" , views.alumnos , name="alumnos" ),
    path("contacto" , views.contacto),
    #path("alta_curso/<nombre>" , views.alta_curso),
    path("alta_curso" , views.curso_formulario),
    path("buscar_curso" , views.buscar_curso),
    path("buscar" , views.buscar),
    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path("editar_curso/<int:id>" , views.editar , name="editar_curso"),
    path("editar_curso" , views.editar ,name="editar_curso"),
    path("login" , views.login_request , name="Login"),
    path("register" , views.register , name="Register"),
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("about", views.about , name="about"),
    path("pages", views.pages , name="pages"),
    path("messages", views.messages , name="messages"),
    path("lista_pages", views.lista_pages),
    path("alta_pages", views.page_formulario),
    path("elimina_page/<int:id>" , views.elimina_page , name="elimina_page"),
    path("buscar_page" , views.buscar_page , name="buscar_page"),
    path("buscar_p" , views.buscar_p),
    path("leer_mas/", views.leer_mas , name="leer"),
    path("editar_page/<int:id>" , views.editar_page, name="editar_page") ,
    path("editar_page/" , views.editar_page, name="editar_page") ,
    path("perfil" , views.accounts, name="perfil") ,
    path("editarPerfil" , views.editarPerfil , name="editarPerfil")

]
