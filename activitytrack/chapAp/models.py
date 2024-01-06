from django.db import models

# Create your models here.
class Scc(models.Model):
    name = models.CharField(max_length=100)
   
    class Meta:
        app_label = 'chapAp'

class Association(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        app_label = 'chapAp'


class Ministry(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        app_label = 'chapAp'


class Member(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=255)
    Scc = models.ForeignKey(Scc, on_delete=models.CASCADE)
    Ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    Association = models.ForeignKey(Association, on_delete=models.CASCADE)

    class Meta:
        app_label = 'chapAp'
