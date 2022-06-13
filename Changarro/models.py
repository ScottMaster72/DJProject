from django.db import models

# Create your models here.
class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre:")
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen:", null=True,)
    descripcion = models.TextField(verbose_name="Descripcion:", null=True)

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + "Descripcion: " + self.descripcion
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre:")
    telefono = models.CharField(max_length=10, verbose_name="Telefono:")
    email = models.EmailField(verbose_name="Correo Electronico:")
    contraseña = models.CharField(max_length=100, verbose_name="Contraseña:")

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + "Correo Electronico: " + self.email
        return fila


class Proovedores(models.Model):
    ID = models.AutoField(primary_key=True)
    Empresa = models.CharField(max_length=100, verbose_name="Empresa:")
    Telefono = models.CharField(max_length=100, verbose_name="Telefono:")
    Orden = models.CharField(max_length=100, verbose_name="Orden:")
    Entregado = models.CharField(max_length=50, verbose_name="Entregado:")

    def __str__(self):
        fila = "Empresa: " + self.Empresa + " - " + "Entregado: " + self.Entregado
        return fila


class Sucursales(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100, verbose_name="Nombre:")
    Direccion = models.CharField(max_length=100, verbose_name="Direccion:")
    Telefono = models.CharField(max_length=100, verbose_name="Telefono:")

    def __str__(self):
        fila = "Nombre: " + self.Nombre + " - " + "Direccion: " + self.Direccion
        return fila


class Consola(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100, verbose_name="Nombre:")
    Serie = models.CharField(max_length=100, verbose_name="Serie:")
    Imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen:", null=True,)
    Descripcion = models.TextField(verbose_name="Descripcion:", null=True)

    def __str__(self):
        fila = "Nombre: " + self.Nombre + " - " + "Descripcion: " + self.Descripcion
        return fila

    def delete(self, using=None, keep_parents=False):
        self.Imagen.storage.delete(self.Imagen.name)
        super().delete()


class Promociones(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100, verbose_name="Nombre:")
    Fecha = models.DateField(verbose_name="Fecha:")
    Descripcion = models.TextField(verbose_name="Descripcion:", null=True)
    Descuento = models.CharField(max_length=100, verbose_name="Descuento:")

    def __str__(self):
        fila = "Nombre: " + self.Nombre + " - " + "Descripcion: " + self.Descripcion
        return fila


class Merma(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100, verbose_name="Nombre:")
    Observaciones = models.TextField(verbose_name="Observaciones:", null=True)


class Pedido(models.Model):
    Id = models.AutoField(primary_key=True)
    Descripcion = models.TextField(verbose_name="Descripcion:", null=True)
    Fecha = models.DateField(verbose_name="Fecha:")
    Estatus = models.CharField(max_length=100, verbose_name="Estatus:")

    def __str__(self):
        fila = "Descripcion: " + self.Descripcion + " - " + "Estatus: " + self.Estatus
        return fila