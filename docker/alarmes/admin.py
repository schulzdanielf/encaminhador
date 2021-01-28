from django.contrib import admin
from alarmes.models import Evento, Incidente

class Eventos(admin.ModelAdmin):
    list_display = ('id', 'Description', 'OpenTime')
    list_display_links = ('id', 'Description','OpenTime')
    search_fields = ('Description',)
    list_per_page = 20

admin.site.register(Evento, Eventos)

class Incidentes(admin.ModelAdmin):
    list_display = ('id', 'Description', 'OpenTime', 'Hostname')
    list_display_links = ('id', 'Description', 'OpenTime', 'Hostname')
    search_fields = ('Description',)
    list_per_page = 20

admin.site.register(Incidente, Incidentes)
