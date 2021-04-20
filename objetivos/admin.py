from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Objetivo, Data, Estructura, Preferencia, Tipofuncion, Indicador, Parametro

admin.site.register(Preferencia)
admin.site.register(Tipofuncion)
admin.site.register(Indicador)
admin.site.register(Parametro)


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ['indicador', 'creator', 'value', 'datetime']
    list_editable = ['value', 'datetime']


admin.site.register(
    Objetivo,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)

admin.site.register(
    Estructura,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)
