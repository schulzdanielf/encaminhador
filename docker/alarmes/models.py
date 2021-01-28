from django.db import models
from datetime import datetime

# Create your models here.
class Evento(models.Model):

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
    OpenedBy = models.CharField(max_length=100, default="", editable=False)
    Service = models.CharField(max_length=1000, default="", editable=False)
    Status = models.CharField(max_length=1000, default="", editable=False)
    Subarea = models.CharField(max_length=1000, default="", editable=False)
    TelefoneSolicitante = models.CharField(max_length=1000, default="", editable=False)
    Title  = models.CharField(max_length=1000, default="", editable=False)
    UpdateBy = models.CharField(max_length=1000, default="", editable=False)
    UpdateTime  = models.DateTimeField(default=datetime.now(), editable=False)
    Urgency = models.CharField(max_length=100, default="", editable=False)


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
#    action = models.CharField(max_length=1000)

    Hostname = models.CharField(max_length=100)
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

    def __str__(self):
        return self.action
