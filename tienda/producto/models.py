from django.db import models

# Create your models here.

class Peluche(models.Model):
    id_peluche      = models.AutoField(db_column='id_peluche', primary_key=True)
    nombre_peluche = models.CharField(max_length=20,blank=True, null=True)
    medida              = models.CharField(max_length=20,blank=True)
    precio = models.IntegerField(blank=True, null=True)
    tamano = models.IntegerField(blank=True, null=True)

    foto             = models.ImageField(upload_to='fotos', blank=True, null=True)

    activo           = models.IntegerField(blank=True, null=True)

class Almohada(models.Model):
    id_almohada     = models.AutoField(db_column='id_almohada', primary_key=True)
    nombre_almohada = models.CharField(max_length=20,blank=True, null=True)
    medida = models.CharField(max_length=20, blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    material = models.IntegerField(blank=True, null=True)

    foto             = models.ImageField(upload_to='fotos', blank=True, null=True)

    activo           = models.IntegerField(blank=True, null=True)

class Daikimakura(models.Model):
    id_daiki     = models.AutoField(db_column='id_daikimakura', primary_key=True)
    nombre_daiki = models.CharField(max_length=20,blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    genero = models.IntegerField(blank=True, null=True)

    foto             = models.ImageField(upload_to='fotos', blank=True, null=True)

    activo           = models.IntegerField(blank=True, null=True)

class Usuario(models.Model):
    id_usuario     = models.AutoField(db_column='id_usuario', primary_key=True)
    nombre = models.CharField(max_length=20,blank=True, null=True)
    apellido = models.CharField(max_length=20,blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    email             = models.CharField(max_length=20,blank=True, null=True)
    contraseña           = models.CharField(max_length=20,blank=True, null=True)

