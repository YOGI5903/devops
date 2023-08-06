from django.db import models

# Create your models here.
class Newapp(models.Model):
    firstname=models.CharField(max_length=545)
    lastname=models.CharField(max_length=452)
class Todo(models.Model):
    work=models.CharField(max_length=500)
   