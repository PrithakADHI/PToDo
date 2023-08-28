from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    user_name = models.CharField(max_length=200, default="hello")
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)


class Users(models.Model):
    name = models.CharField(max_length=200)