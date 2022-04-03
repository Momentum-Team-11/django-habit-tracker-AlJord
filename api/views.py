
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from habit.models import Habit, Result, User
from .serializers import HabitResultSerializer, HabitSerializer, ResultSerializer, UserSerializer
from api import serializers


class HabitListView(generics.ListCreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class ResultListView(generics.ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class HabitDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitResultSerializer

class ResultDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

