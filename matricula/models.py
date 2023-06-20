from django.db import models

# Create your models here.
class PlaEstudi(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Modul(models.Model):
    studie = models.ForeignKey(PlaEstudi, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class UnitatFormativa(models.Model):
    module = models.ForeignKey(Modul, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    hours = models.IntegerField(default=0)
    def __str__(self):
        return self.name