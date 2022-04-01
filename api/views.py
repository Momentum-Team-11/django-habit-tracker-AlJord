
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from habit.models import Habit, Result, User
from .serializers import HabitResultSerializer, HabitSerializer, ResultSerializer, UserSerializer
from api import serializers


class HabitListView(generics.ListCreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    def perform_create(self, serializer):
        serializer.save(app_user=self.request.user)

class ResultListView(generics.ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class HabitDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitResultSerializer
    def preform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

