from rest_framework import viewsets
from alarmes.models import Evento, Incidente
from alarmes.serializer import EventoSerializer, IncidenteSerializer
import os
from rest_framework.response import Response
from alarmes.classificador import Classificador
import requests
from django.http import HttpResponse
from alarmes.criador import Criador


class EventosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os eventos"""
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    def index(request):
        return HttpResponse()

    def create(self, request):
        action = self.request.data.get('action')
        
        #os.system('python cout.py '+action)
        try:
            equipe = Classificador.classifica(action)
        except:
            return Response({"status_code":405, "Message": "Campo action preenchido inválido"})

        url = 'http://localhost:8123/incidente/'
        json = Criador.cria_incidente(self.request)
        json['equipe'] = equipe
        json['hostname'] = 'teste'

#        myobj = {'action':action, 'equipe':equipe, 'hostname':'POSTMAN'}


        x = requests.post(url, data = json)


        return Response(
            {
                "status_code":x.status_code, 'equipe':equipe, "json": json
            }
        )

class IncidentesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os incidentes"""
    queryset = Incidente.objects.all()
    serializer_class = IncidenteSerializer

    def index(request):
        return HttpResponse()
