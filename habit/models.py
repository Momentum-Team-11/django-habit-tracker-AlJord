from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class User(AbstractUser):
    def __str__(self):
        return self.username

class Habit(models.Model):
    goal=models.CharField(max_length=300)
    created_at=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.goal


class Result(models.Model):
    habit=models.ForeignKey(Habit,on_delete=models.CASCADE, related_name="results") #users will see which goal was completed
    total=models.CharField(max_length=20,default="",null=True, blank=True) #Users can see total number of goals completed
    def __str__(self):
        return self.total


