from django.db import models

# Create your models here.
class Users(models.Model):
    #id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=40)

class Posts(models.Model):
    # id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_time = models.IntegerField()
    username = models.CharField(max_length=50)
