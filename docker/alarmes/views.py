from rest_framework import viewsets
from alarmes.models import Evento, Incidente
from alarmes.serializer import EventoSerializer, IncidenteSerializer
import os
from rest_framework.response import Response
from alarmes.classificador import Classificador
import requests
from django.http import HttpResponse
from alarmes.processa import Processa
from alarmes.aviso  import Aviso

class EventosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os eventos"""
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    def index(request):
        return HttpResponse()

    def create(self, request):

#        try:
        json = Processa.cria_incidente(self.request)
#        except:
#            return Response({"status_code":405, "Message": "Algum erro ocorreu no processamento"})
        aviso = Aviso()
        if json['Hostname'] is not None:
            if aviso.busca_hostname_aberto(json['Hostname']) > 0:
                return Response({"status_code":407, "Message": "Existe um incidente aberto para este hostname no GSTI"})
        else:
            return Response({"status_code":406, "Message": "Não foi possível localizar o hostname do Incidente"})


        url = 'http://localhost:8123/incidente/'

#        json['Hostname'] = 'teste'

#        myobj = {'action':action, 'equipe':equipe, 'hostname':'POSTMAN'}


        x = requests.post(url, data = json)


        return Response(
            {
                "status_code":x.status_code, 'equipe':json['AssignmentGroup']
            }
        )

class IncidentesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os incidentes"""
    queryset = Incidente.objects.all()
    serializer_class = IncidenteSerializer

    def index(request):
        return HttpResponse()
