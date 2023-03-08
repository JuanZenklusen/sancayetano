from django.db import models
from datetime import date

class Cronograma(models.Model):
    cronograma = models.CharField(max_length=50, blank=False, null=False)
    date = models.DateField(default=date.today)
    
    def __str__(self):
        return self.cronograma
    
class Capilla(models.Model):
    nombre_sede = models.CharField(max_length=50, blank=False, null=False)
    
    def __str__(self):
        return self.nombre_sede

class Musico(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    contacto = models.CharField(max_length=50, blank=False, null=False)
    
    def __str__(self):
        return self.nombre

class Misa(models.Model):
    fecha = models.DateField(blank=False, null=False)
    horario = models.CharField(max_length=6, blank=False, null=False)
    responsable = models.CharField(max_length=50, blank=True, null=True)
    observaciones = models.CharField(max_length=150, blank=True, null=True)
    cronograma = models.ForeignKey(Cronograma, on_delete=models.CASCADE)
    capilla = models.ForeignKey(Capilla, on_delete=models.CASCADE)
    musico = models.ForeignKey(Musico, on_delete=models.CASCADE)