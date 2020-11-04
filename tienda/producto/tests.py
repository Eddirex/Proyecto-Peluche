import unittest
from producto.models import Peluche
from producto.models import Usuario



class testPeluche(unittest.TestCase):


#creacion de peluches
    #"""
    def test_crear_peluches(self):
        peluche = Peluche.objects.create(nombre_peluche='Tigrex',
                                       medida='10x8x17cm',
                                       precio=32990,
                                       tamano=1,
                                       foto='file:///C:/Users/user/Desktop/ProyectoPeluches/tienda/tienda/static/imagen/productos/tigrex.jpg',
                                       activo=1,
                                       )
        peluche.save()

        self.assertTrue(peluche,True)

        peluche = Peluche.objects.create(nombre_peluche='Teostra',
                                       medida='8x10x17cm',
                                       precio=32990,
                                       tamano=1,
                                       foto='file:///C:/Users/user/Desktop/ProyectoPeluches/tienda/tienda/static/imagen/productos/teostra.jpg',
                                       activo=1,
                                       )
        peluche.save()
        self.assertTrue(peluche,True)
        peluche = Peluche.objects.create(nombre_peluche='Rathalos',
                                       medida='15x12x20cm',
                                       precio=32990,
                                       tamano=2,
                                       foto='file:///C:/Users/user/Desktop/ProyectoPeluches/tienda/tienda/static/imagen/productos/rathalos.jpg',
                                       activo=1,
                                       )
        peluche.save()

        peluche = Peluche.objects.create(nombre_peluche='Rathian',
                                       medida='15x12x20cm',
                                       precio=32990,
                                       tamano=2,
                                       foto='file:///C:/Users/user/Desktop/ProyectoPeluches/tienda/tienda/static/imagen/productos/rathian.jpg',
                                       activo=1,
                                       )
        peluche.save()
        self.assertTrue(peluche,True)

        peluche = Peluche.objects.create(nombre_peluche='Shiba Inu black',
                                       medida='35x35x50cm',
                                       precio=32990,
                                       tamano=3,
                                       foto='file:///C:/Users/user/Desktop/ProyectoPeluches/tienda/tienda/static/imagen/productos/akita1.jpg',
                                       activo=1,
                                       )
        peluche.save()
        self.assertTrue(peluche,True) 

        peluche = Peluche.objects.create(nombre_peluche='Shiba Inu cafe',
                                       medida='35x35x50cm',
                                       precio=32990,
                                       tamano=3,
                                       foto='file:///C:/Users/user/Desktop/ProyectoPeluches/tienda/tienda/static/imagen/productos/akita2.jpg',
                                       activo=1,
                                       )
        peluche.save()
        self.assertTrue(peluche,True)

        peluche = Peluche.objects.create(nombre_peluche='Shiba Inu gris',
                                       medida='35x35x50cm',
                                       precio=32990,
                                       tamano=3,
                                       foto='file:///file:///C:/Users/user/Desktop/ProyectoPeluches/tienda/tienda/static/imagen/productos/akita3.webp',
                                       activo=0,
                                       )
        peluche.save()
        self.assertTrue(peluche,True)
        #"""
    """  
    def test_eliminar_peluches(self):
        peluche = Peluche.objects.get(nombre_peluche = 'Tigrex')
        if peluche.nombre_peluche == 'Tigrex':

            peluche.delete()
            print("se elimino")    

        else:
            print("no ha sido eliminado")

        peluche = Peluche.objects.get(nombre_peluche = 'Teostra')
        if peluche.nombre_peluche == 'Teostra':

            peluche.delete()
            print("se elimino")    

        else:
            print("no ha sido eliminado")

        peluche = Peluche.objects.get(nombre_peluche = 'Rathalos')
        if peluche.nombre_peluche == 'Rathalos':

            peluche.delete()
            print("se elimino")    

        else:
            print("no ha sido eliminado")

        peluche = Peluche.objects.get(nombre_peluche = 'Rathian')
        if peluche.nombre_peluche == 'Rathian':

            peluche.delete()
            print("se elimino")    

        else:
            print("no ha sido eliminado")

        peluche = Peluche.objects.get(nombre_peluche = 'Shiba Inu black')
        if peluche.nombre_peluche == 'Shiba Inu black':

            peluche.delete()
            print("se elimino")    

        else:
            print("no ha sido eliminado")

        peluche = Peluche.objects.get(nombre_peluche = 'Shiba Inu cafe')
        if peluche.nombre_peluche == 'Shiba Inu cafe':

            peluche.delete()
            print("se elimino")    

        else:
            print("no ha sido eliminado")

        peluche = Peluche.objects.get(nombre_peluche = 'Shiba Inu gris')
        if peluche.nombre_peluche == 'Shiba Inu gris':

            peluche.delete()
            print("se elimino")    

        else:
            print("no ha sido eliminado")
    #"""           
              
