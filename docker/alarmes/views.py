from rest_framework import viewsets
from alarmes.models import Evento, Incidente
from alarmes.serializer import EventoSerializer, IncidenteSerializer


class EventosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os eventos"""
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class IncidentesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os incidentes"""
    queryset = Incidente.objects.all()
    serializer_class = IncidenteSerializer