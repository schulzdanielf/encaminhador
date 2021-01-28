from django.test import TestCase, RequestFactory
from django.urls import reverse
from alarmes.views import EventosViewSet, IncidentesViewSet
import requests



class AlarmesURLSTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_rota_url_evento(self):
        """Testa se a página de eventos está disponível"""
        request = self.factory.get('/evento')
        response = EventosViewSet.index(request)
        self.assertEqual(response.status_code, 200)

    def test_rota_url_incidente(self):
        """Testa se a página de eventos está disponível"""
        request = self.factory.get('/incidente')
        response = IncidentesViewSet.index(request)
        self.assertEqual(response.status_code, 200)

    def test_post_evento(self):
        """Testa a API está recebendo eventos e classificando"""
        myobj = {'action':"Data: Tue Nov 03 11:43:14 BRST 2020\nHost: pxl1tbs00012\nID: 85bc26bc-1dda-71eb-1192-ac11d8ae0000\nMensagem: LINUX - Consumo de DISCO = 98.860000%, acima do estabelecido(90%) - FileSystem=/var/log\nInstrucao: Atributo Customizado não cadastrado, verificar no evento campo Instruction.",
         "data_evento": "2020-12-27T19:13:00-03:00", "string_errada":"errado"}

        r = requests.post('http://localhost:8123/evento/', data=myobj)

        self.assertEqual(r.status_code, 200)
