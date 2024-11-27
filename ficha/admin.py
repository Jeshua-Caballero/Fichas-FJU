from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.FichaJoven)
class FichaJovenAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre']

@admin.register(models.PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'departamento', 'es_encargado_nacional', 'es_encargado', 'es_asistente']

@admin.register(models.GrupoEspiritual)
class GrupoEspiritualAdmin(admin.ModelAdmin):
    list_display = ['nombre']