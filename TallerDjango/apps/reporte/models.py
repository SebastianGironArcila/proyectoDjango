from django.db import models

# Create your models here.

from apps.proveedor.models import Proveedor

class Reporte(models.Model):
	cantidadEntregasAnuales = models.IntegerField()
	año = models.IntegerField()
	registrante = models.CharField(max_length=50)

	proveedor = models.ForeignKey(Proveedor,null=True, blank=False, on_delete=models.CASCADE)
	




