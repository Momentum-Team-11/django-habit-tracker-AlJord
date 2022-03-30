from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.db.models import UniqueConstraint
from django.db.models import Q


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"
    def __str__(self):
        return self.username


class Habit(models.Model):
    title=models.CharField(max_length=300,null=True, blank=True)
    goal=models.CharField(max_length=300,null=True, blank=True)
    daily=models.IntegerField(default=0)
    created_at=models.DateField(auto_now_add=True) #auto_now_add look up what default does
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True, related_name='habits')
    def __str__(self):
        return self.title if self.title else ''


class Result(models.Model):
    
    habit=models.ForeignKey(Habit,on_delete=models.CASCADE, related_name="results") #users will see which goal was completed
    total=models.IntegerField(default=0) 
    accomplished=models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
        models.UniqueConstraint(fields=['habit','accomplished'], name='one_record_per_day')
        ]
    def __str__(self):
        return str(self.total)


