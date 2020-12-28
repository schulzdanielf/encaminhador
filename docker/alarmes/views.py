from rest_framework import viewsets
from alarmes.models import Evento, Incidente
from alarmes.serializer import EventoSerializer, IncidenteSerializer
import os
from rest_framework.response import Response
from alarmes.classificador import Classificador
import requests


class EventosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os eventos"""
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    def create(self, request):
        action = self.request.data.get('action')
        #os.system('python cout.py '+action)
        equipe = Classificador.classifica(action)
        url = 'http://localhost:8123/incidente/'
        myobj = {'action':action, 'equipe':equipe, 'hostname':'POSTMAN'}
        x = requests.post(url, data = myobj)


        return Response(
            {
                "Status":True, 'equipe':equipe
            }
        )

class IncidentesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os incidentes"""
    queryset = Incidente.objects.all()
    serializer_class = IncidenteSerializer
