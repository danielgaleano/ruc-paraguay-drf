from django.db import models


class Ruc(models.Model):
    numero = models.CharField("Nro. de RUC", max_length=32)
    nombre = models.CharField("Nombre o Denominacion", max_length=512)
    dv = models.CharField("Digito verificador", max_length=1)
    numero_anterior = models.CharField("Nro anterior", max_length=32)
    estado = models.CharField("Estado", max_length=32)


