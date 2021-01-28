from django.contrib import admin
from alarmes.models import Evento, Incidente

class Eventos(admin.ModelAdmin):
    list_display = ('id', 'action', 'data_evento', 'Ambiente')
    list_display_links = ('id', 'action', 'data_evento', 'Ambiente')
    search_fields = ('action',)
    list_per_page = 20

admin.site.register(Evento, Eventos)

class Incidentes(admin.ModelAdmin):
    list_display = ('id', 'action', 'equipe', 'hostname')
    list_display_links = ('id', 'action', 'equipe', 'hostname')
    search_fields = ('action',)
    list_per_page = 20

admin.site.register(Incidente, Incidentes)
