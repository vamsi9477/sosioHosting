from django.db import models

# Create your models here.

class Sosio(models.Model):
    no=models.IntegerField(default=5,primary_key=True)
    date=models.DateField()
    amount=models.IntegerField(default=5)
    names=models.CharField(max_length=100)
    res=models.IntegerField()