from django.shortcuts import render
from .models import Peluche
from .models import Almohada
from .models import Daikimakura
from .models import Usuario


# Create your views here.

def index(request):
    print("Index")
    context={}
    return render(request,'producto/index.html',context)

def crear_cuenta(request):
    print("crear_cuenta")
    context={}
    return render(request,'producto/crear_cuenta.html',context)

def almohada(request):
    print("almohada")
    context={}
    return render(request,'producto/almohada.html',context)

def daikimakura(request):
    print("daikimakura")
    context={}
    return render(request,'producto/daikimakura.html',context)

def crud(request):
    print("crud")
    context={}
    return render(request,'producto/crud/crud.html',context)

def añadir(request):
    print("añadir")
    context={}
    return render(request,'producto/crud/añadir.html',context)

def modificar(request):
    print("modificar")
    context={}
    return render(request,'producto/crud/modificar.html',context)

def eliminar(request):
    print("eliminar")
    context={}
    return render(request,'producto/crud/eliminar.html',context)

def peluche(request):
    print("peluche")
    lista = Peluche.objects.filter(activo =1)
    context={'listado':lista}
    return render(request,'producto/peluche.html',context)

def peluche_pequeño(request):
    print("peluche pequeño")
    lista = Peluche.objects.filter(activo =1, tamano="1")
    context={'listado':lista}
    return render(request,'producto/peluche.html',context)

def peluche_mediano(request):
    print("peluche mediano")
    lista = Peluche.objects.filter(activo =1, tamano=2)
    context={'listado':lista}
    return render(request,'producto/peluche.html',context)

def peluche_grande(request):
    print("peluche grande")
    lista = Peluche.objects.filter(activo ="1", tamano="3")
    context={'listado':lista}
    return render(request,'producto/peluche.html',context)


# CRUD

def añadir_p(request):
    print("añadir_p")
    if request.method == 'POST':
       _nom_peluche = request.POST['nombre_peluche']
       _medida = request.POST['medida']
       _precio =request.POST['precio']
       _tamano =request.POST['tamano']
       _foto = request.FILES['foto']
       _activo =request.POST['activo']

       if _nom_peluche != "":
           try:
               peluche = Peluche()

               peluche.nombre_peluche = _nom_peluche
               peluche.medida = _medida
               peluche.precio = _precio
               peluche.tamano = _tamano
               peluche.foto = _foto
               peluche.activo = _activo

               peluche.save()

               return render(request, 'producto/mensaje/guardado_exito.html',{})

           except peluche.DoesNotExist:
               return render(request, 'personas/mensaje/error.html', {})


def listar_todo(request):
    print("listar productos")
    #lista = Alumno.objects.all()
    lista = Peluche.objects.filter()
    context={'listado':lista}
    return render(request,'producto/crud/listar.html',context)

def eliminar_modificar(request):
    print("listar productos")
    la_id = request.POST['id']
    #lista = Alumno.objects.all()
    peluche = Peluche.objects.get(id_peluche = la_id)
    context={'peluche':peluche}
    return render(request,'producto/crud/up_del.html',context)

def mod_del(request):

    print("modificar o eliminar")
    if request.method == 'POST':

        print(request.POST['boton'])
        _id = request.POST['id']
        _nom_peluche = request.POST['nombre_peluche']
        _medida = request.POST['medida']
        _precio =request.POST['precio']
        _tamano =request.POST['tamano']
        _foto = request.FILES['foto']
        _activo =request.POST['activo']

        if request.POST['boton'] == 'eliminar':
            try:
                print("estamos en el try de eliminar")
                peluche = Peluche()
                peluche = Peluche.objects.get(id_peluche = _id)
                if peluche is not None:
                    print("Peluche")
                    peluche.delete()      
                    return render(request,'producto/mensaje/eliminado.html',{})
            except peluche.DoesNotExist:
               return render(request, 'producto/mensaje/error.html', {})
                    
        elif request.POST['boton'] == 'modificar':
            try:
                peluche = Peluche()

                peluche.id_peluche = _id
                peluche.nombre_peluche = _nom_peluche
                peluche.medida = _medida
                peluche.precio = _precio
                peluche.tamano = _tamano
                peluche.foto = _foto
                peluche.activo = _activo

                peluche.save()

                return render(request, 'producto/mensaje/guardado_exito.html',{})
            except peluche.DoesNotExist:
               return render(request, 'producto/mensaje/error.html', {})

#creacion de usuario

def añadir_u(request):
    print("añadir_usuario")
    if request.method == 'POST':
       _nombre = request.POST['nombre_peluche']
       _apellido = request.POST['medida']
       _edad =request.POST['precio']
       _email =request.POST['tamano']
       _contraseña =request.POST['activo']

       if _nombre != "":
           try:
               usuario = Peluche()

               usuario.nombre = _nombre
               usuario.apellido = _apellido
               usuario.edad = _edad
               usuario.email = _email
               usuario.contraseña = _contraseña

               usuario.save()

               return render(request, 'producto/mensaje/guardado_exito.html',{})

           except usuario.DoesNotExist:
               return render(request, 'personas/mensaje/error.html', {})




        

        