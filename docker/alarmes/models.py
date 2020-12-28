from django.db import models

# Create your models here.
class Evento(models.Model):
    action = models.CharField(max_length=1000)
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

    def __str__(self):
        return self.action
