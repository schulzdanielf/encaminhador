from django.db import models
from datetime import datetime

# Create your models here.
class Evento(models.Model):
    action = models.CharField(max_length=1000)
    Description = models.CharField(max_length=1000, default="")
    Ambiente = models.CharField(max_length=100, default="")
    Area = models.CharField(max_length=1000, default="", editable=False)
    Assignee = models.CharField(max_length=1000, default="", editable=False)
    AssignmentGroup = models.CharField(max_length=1000, default="", editable=False)
    Category = models.CharField(max_length=1000, default="", editable=False)
    Contact = models.CharField(max_length=1000, default="", editable=False)
    Description = models.CharField(max_length=1000, default="", editable=False)
    EquipeCriador = models.CharField(max_length=1000, default="", editable=False)
    Impact = models.CharField(max_length=1000, default="", editable=False)
    IncidentID = models.CharField(max_length=100, default="", editable=False)
    OpenTime = models.DateTimeField(default=datetime.now(), editable=False)
    #OpenTime = models.DateTimeField(default='2021-01-01 00:00', editable=False)
    OpenedBy = models.CharField(max_length=100, default="", editable=False)
    Service = models.CharField(max_length=1000, default="", editable=False)
    Status = models.CharField(max_length=1000, default="", editable=False)
    Subarea = models.CharField(max_length=1000, default="", editable=False)
    TelefoneSolicitante = models.CharField(max_length=1000, default="", editable=False)
    Title  = models.CharField(max_length=1000, default="", editable=False)
    UpdateBy = models.CharField(max_length=1000, default="", editable=False)
    UpdateTime  = models.DateTimeField(default=datetime.now(), editable=False)
    Urgency = models.CharField(max_length=100, default="", editable=False)
    data_evento = models.DateTimeField()

    def __str__(self):
        return self.action

    def post(self, request):
        action = self.request.POST.get('action','')
        os.system('python cout.py '+action)
        return Response(
            {
                "Status":True
            }
        )

class Incidente(models.Model):
    action = models.CharField(max_length=1000)
    EQUIPE = (
        ('0', 'GSERV-AU'),
        ('1', 'DAT-SP'),
        ('2', 'GPROM-31'),
        ('3', 'GPROM-32'),
        ('4', 'GPROM-33'),
        ('5', 'GPROM-35'),
        ('6', 'GPROM-72'),
    )
    equipe = models.CharField(max_length=1, choices=EQUIPE, blank=False, null=False,default='1')
    hostname = models.CharField(max_length=100)
    Ambiente = models.CharField(max_length=100, default="")
    Area = models.CharField(max_length=1000, default="")
    Assignee = models.CharField(max_length=1000, default="")
    AssignmentGroup = models.CharField(max_length=1000, default="")
    Category = models.CharField(max_length=1000, default="")
    Contact = models.CharField(max_length=1000, default="")
    Description = models.CharField(max_length=1000, default="")
    EquipeCriador = models.CharField(max_length=1000, default="")
    Impact = models.CharField(max_length=1000, default="")
    IncidentID = models.CharField(max_length=100, default="")
    OpenTime = models.DateTimeField(default=datetime.now())
    OpenedBy = models.CharField(max_length=100, default="")
    Service = models.CharField(max_length=1000, default="")
    Status = models.CharField(max_length=1000, default="")
    Subarea = models.CharField(max_length=1000, default="")
    TelefoneSolicitante = models.CharField(max_length=1000, default="")
    Title  = models.CharField(max_length=1000, default="")
    UpdateBy = models.CharField(max_length=1000, default="")
    UpdateTime  = models.DateTimeField(default=datetime.now())
    Urgency = models.CharField(max_length=100, default="")
    data_evento = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.action
