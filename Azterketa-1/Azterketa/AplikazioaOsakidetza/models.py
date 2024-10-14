from django.db import models
from django.utils import timezone

class Paziente(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=75)
    abizena = models.CharField(max_length=100)
    jaiotze_data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.izena} {self.abizena}"
    
class Medikua(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=75)
    abizena = models.CharField(max_length=100)
    jaiotze_data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.izena} {self.abizena}"

class Zitak(models.Model):
    id = models.AutoField(primary_key=True)
    zita_data = models.DateTimeField(default=timezone.now)
    pazientekodea=models.ForeignKey(Paziente, on_delete=models.CASCADE)
    medikukodea=models.ForeignKey(Medikua, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.pazientekodea} zita dauka {self.medikukodea} -ekin {self.zita_data}"