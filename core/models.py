from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta, time,date


# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __srt__(self):
        return self.titulo
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%MHrs')
    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y/%m/%d')

    def get_evento_atrasado(self):
        data= self.data_evento
        if datetime.combine(date(data), time(0, 0,0,0)) < datetime.now():
            return True
        else:
            return False

