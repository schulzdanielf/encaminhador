from django.contrib import admin
from django.urls import path, include
from alarmes.views import EventosViewSet, IncidentesViewSet
from rest_framework import routers

router =  routers.DefaultRouter()
router.register('evento', EventosViewSet, basename='Eventos')
router.register('incidente', IncidentesViewSet, basename='Incidentes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
