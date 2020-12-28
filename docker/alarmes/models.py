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
        ('1', 'GPROM-31'),
        ('2', 'GPROM-32'),
        ('3', 'GPROM-33'),
        ('4', 'GPROM-35'),
        ('5', 'GPROM-73'),
        ('6', 'GSERV-AU'),
        ('7', 'DAT-SP')
    )
    equipe = models.CharField(max_length=1, choices=EQUIPE, blank=False, null=False,default='1')
    hostname = models.CharField(max_length=100)

    def __str__(self):
        return self.action
