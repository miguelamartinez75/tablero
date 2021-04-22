from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel
from treewidget.fields import TreeForeignKey


class Objetivo(MPTTModel):
    name = models.CharField(max_length=500)
    createdAt = models.DateTimeField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    tiene_indicador = models.BooleanField()
    id_indicador = models.ForeignKey('Indicador', on_delete=models.CASCADE, null=True, blank=True)
    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Estructura(MPTTModel):
    name = models.CharField(max_length=200)
    mission = models.TextField(blank=True)
    function = models.TextField(blank=True)
    decreto = models.CharField(max_length=50, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Preferencia(models.Model):
    name = models.CharField(max_length=100)
    objetivo = models.ForeignKey(Objetivo, on_delete=models.CASCADE)
    parent = models.ForeignKey(Estructura, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Tipofuncion(models.Model):
    name = models.CharField(max_length=50)
    func = models.CharField(max_length=255)

    def __str__(self):
        return self.name + f" ({self.func})"

    class Meta:
        ordering = ['name']


class Indicador(models.Model):
    name = models.CharField(max_length=100)
    tipofuncion = models.ForeignKey(Tipofuncion, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "%s %s" %(self.id, self.name)

    class Meta:
        ordering = ['name']


class Parametro(models.Model):
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE, blank=True, null=True)
    parama = models.FloatField(null=True, blank=True)
    paramb = models.FloatField(null=True, blank=True)
    paramc = models.FloatField(null=True, blank=True)
    paramd = models.FloatField(null=True, blank=True)
    vigencia = models.DateTimeField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='param_creator')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        # ordering = ('-created',)

    def __str__(self):
        return "%s %s" % (self.indicador.name, self.vigencia)

class Data(models.Model):
    datetime = models.DateTimeField()
    detail = models.CharField(max_length=250, null=True, blank=True)
    value = models.FloatField(null=True, blank=True)
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE, blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='data_creator')

    def __str__(self):
        return self.indicador.name + " - " + str(self.datetime)

