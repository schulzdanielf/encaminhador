from django.test import TestCase, RequestFactory
from django.urls import reverse
from alarmes.views import EventosViewSet, IncidentesViewSet


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
