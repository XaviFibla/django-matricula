from django.db import models

# Create your models here.
class PlaEstudi(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Modul(models.Model):
    studie = models.ForeignKey(PlaEstudi, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    
class UnitatFormativa(models.Model):
    module = models.ForeignKey(Modul, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    hours = models.IntegerField(default=0)