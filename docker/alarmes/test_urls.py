from django.test import TestCase, RequestFactory
from django.urls import reverse
from alarmes.views import EventosViewSet, IncidentesViewSet
import requests
from alarmes.aviso import Aviso



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
        myobj ={
                "Ambiente": "Produï¿œï¿œo",
                "Area": "Armazenamento",
                "Assignee": "F0898828",
                "Category": "Incidente",
                "Contact": "f2255270",
                "Description": [
                  "Incidente originado a partir do(s) evento(s) abaixo:",
                  "Data: Tue Dec 29 03:25:11 BRST 2020",
                  "Host: pxw0mssql001",
                  "ID: 38dcf960-4996-71eb-19ec-ac11bfe90000",
                  "Mensagem: WINDOWS - Consumo de DISCO = 90,000000%, acima do estabelecido(90%) - FileSystem=M:MSSQLDATA_OPCAS03_01",
                  "Instrucao: https://ci.bb.com.br/novo/index.php/SOLUï¿œï¿œO:TI/Windows/Incidentes"
                ],
                "EquipeCriador": "DITEC/UOS/GPROM/D3/E33/N2 SO HIGH-END",
                "Impact": "Baixo",
                "IncidentID": "RDI20200051497",
                "OpenedBy": "HPOMI",
                "Service": "266382",
                "Status": "Encaminhado",
                "Subarea": "Estouro de ï¿œrea alocada/falta de espaï¿œo",
                "TelefoneSolicitante": "31086146",
                "Title": "[pxw0mssql001] - WINDOWS - Consumo de DISCO = 90,000000%, acima do estabelecido(90%) - FileSystem=M:MSSQLDATA_OPCAS03_01",
                "UpdatedBy": "HPOMI",
                "UpdatedTime": "2020-12-29T07:18:56-03:00",
                "Urgency": "Baixo"
              }

        r = requests.post('http://localhost:8123/evento/', data=myobj)
        print(r.status_code, r.raise_for_status()  )
        self.assertEqual(r.status_code, 200)

    def test_postgres_rdis_connection(self):
        aviso = Aviso()
        aviso.consulta_incidentes()
        if aviso.busca_hostname_aberto('pxl1big00025') < 1:
            self.fail("Não possui incidente aberto para o hostname pxl1big00025")
        aviso.close_connection()
