from django.db import models

# Create your models here.
class product(models.Model):
    pid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=100)
    pcost=models.DecimalField(max_digits=10,decimal_places=2)
    pcolor=models.CharField(max_length=100)
