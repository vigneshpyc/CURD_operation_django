from django.db import models
from app.mongo import db

# Create your models here.
first_collection = db['curd']

class user(models.Model):
    name = models.CharField(max_length=100)
    Age = models.IntegerField()