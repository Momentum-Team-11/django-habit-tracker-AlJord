from rest_framework.views import APIView
from rest_framework.response import Response
from habit.models import Habit
from .serializers import HabitSerializer
from rest_framework.generics import ListAPIView


class HabitListView(ListAPIView):
    queryset = Habit.objects.all()
    searilizer_class = HabitSerializer