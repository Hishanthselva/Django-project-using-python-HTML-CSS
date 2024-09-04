from django.db import models

# Create your models here.
class friends(models.Model):
	no=models.IntegerField()
	name=models.CharField(max_length=64)
	age=models.IntegerField()
	city=models.CharField(max_length=64)
