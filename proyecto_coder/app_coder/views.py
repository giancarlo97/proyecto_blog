from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso , Avatar , Pages
from django.template import loader
from app_coder.forms import Curso_formulario , UserEditForm , Pages_formulario
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required 

# Create your views here.


def inicio(request):

    return render( request , "padre.html" )


@login_required
def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos" : cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )


def alta_curso(request, nombre):
    curso = Curso(nombre=nombre , camada=287318)
    curso.save()
    texto = f"Se guardo en la BD el Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(texto)


def alumnos(request):

    return render( request , "alumnos.html" )


def contacto(request):

    return render( request , "contacto.html" )   

def profesores(request):

    return render( request , "profesores.html" )   



def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            curso = Curso( nombre=datos['nombre'] , camada=datos['camada'])
            curso.save()

            return render( request , "formulario.html")

    return render( request, "formulario.html")





def buscar_curso(request):

    return render( request , "buscar_curso.html")



def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html" , {"cursos": cursos})
    else:
        return HttpResponse("Campo vacio")


def elimina_curso( request , id):

    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()

    return render(request , "cursos.html" , {"cursos": curso})



def editar( request , id):

    curso = Curso.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos['nombre']
            curso.camada = datos['camada']
            curso.save()

            curso = Curso.objects.all()          
            return render(request , "cursos.html" , {"cursos": curso})
    else:
        mi_formulario = Curso_formulario(initial={'nombre':curso.nombre , "camada":curso.camada})
    
    return render( request , "editar_curso.html" , {"mi_formulario":mi_formulario, "curso": curso})



def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request , data= request.POST)

        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request,user)
                avatares = Avatar.objects.filter(user=request.user.id)
                return render( request , "inicio.html" , {"url":avatares[0].imagen.url})
    
            else:
                return HttpResponse(f"Usuario Incorrecto")
        else:         
            return HttpResponse(f"FORM INCORRECTO {form}")

    form = AuthenticationForm()

    return render( request , "login.html" , {"form":form})




def register(request):

    if request.method == "POST":
        
        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()
            return HttpResponse("Usuario creado")




    else:
        form = UserCreationForm()
    return render( request , "registro.html" , {"form":form})


@login_required
def editarPerfil(request):
    
    usuario = request.user

    if request.method == "POST":

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return render( request , "inicio.html")

    else: 
        miFormulario = UserEditForm(initial = {'email':usuario.email})

    return render( request , "editar_perfil.html" , {"miFormulario":miFormulario , "usuario":usuario})

def about(request):
    return render (request,"about.html")

@login_required
def pages(request):
    pages = Pages.objects.all()
    dicc = {"pages" : pages}
    plantilla = loader.get_template("pages.html")
    documento =plantilla.render(dicc) 
    return HttpResponse( documento )

@login_required
def messages(request):
    return render (request,"messages.html")

def lista_pages(request):
    
    pages = Pages.objects.all()
    datos_p = { "datos_p":pages }

    return render (request, "lista_pages.html" , datos_p)

def alta_pages(request, nombre):
    page = Pages(nombre=nombre , camada=11000)
    page.save()
    texto = f"Se guardo en la BD la Page: {page.nombre} Camada: {page.camada}"
    return HttpResponse(texto)

def elimina_page( request , id):

    page = Pages.objects.get(id=id)
    page.delete()

    page = Pages.objects.all()

    return render(request , "pages.html" , {"pages": page})

def page_formulario(request):

    if request.method == "POST":

        mi_formulariop = Pages_formulario( request.POST )

        if mi_formulariop.is_valid():
            datos_p = mi_formulariop.cleaned_data          
            
            page = Pages( nombre=datos_p['nombre'] , camada=datos_p['camada'])
            page.save()

            return render( request , "formulario_page.html")

    return render( request, "formulario_page.html")

def editar_page( request , id):

    page = Pages.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Pages_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            page.nombre = datos['nombre']
            page.camada = datos['camada']
            page.save()

            page = Pages.objects.all()          
            return render(request , "pages.html" , {"pages": page})
    else:
        mi_formulario = Pages_formulario(initial={'nombre':page.nombre , "camada":page.camada})
    
    return render( request , "editar_page.html" , {"mi_formulario":mi_formulario, "page": page})

def buscar_page(request):

    return render( request , "buscar_page.html")

def buscar_p(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        page = Pages.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_page.html" , {"pages": page})
    else:
        return HttpResponse("Campo vacio")

def leer_mas(request):
    
    return render (request, "leer_mas.html")

@login_required
def accounts(request):
    return render (request, "perfil.html")