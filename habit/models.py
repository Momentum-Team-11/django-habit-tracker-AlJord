from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.db.models import UniqueConstraint

class User(AbstractUser):
    def __str__(self):
        return self.username

class Habit(models.Model):
    title=models.CharField(max_length=300,null=True, blank=True)
    goal=models.CharField(max_length=300,null=True, blank=True)
    daily=models.IntegerField(default=0)
    created_at=models.DateField(auto_now_add=True,null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return self.title if self.title else ''


class Result(models.Model):

    habit=models.ForeignKey(Habit,on_delete=models.CASCADE, related_name="results") #users will see which goal was completed
    total=models.IntegerField(default=0) #Users can see total number of goals completed
    attempt=models.BooleanField(False,null=True, blank=True)
    date_accomplished=models.CharField(max_length=20,default="",null=True, blank=True)
    class Meta:
        constraints = [
        models.UniqueConstraint(fields=['habit','date_accomplished'], name='one_record_per_day')
        ]

    def __str__(self):
        return str(self.total)


