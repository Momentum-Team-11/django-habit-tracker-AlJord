from habit.models import Habit, Result, User
from rest_framework import serializers

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            'pk',
            'title',
            'goal',
            'daily',
            'created_at',
        )

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = (
            'pk',
            'habit',
            'total',
            'accomplished'
            )

class HabitResultSerializer(serializers.ModelSerializer):
    results = ResultSerializer(many=True, required=False)
    class Meta:
        model = Habit
        fields = (
            'pk',
            'title',
            'results',
        )

class UserSerializer(serializers.ModelSerializer):
    habits = serializers.PrimaryKeyRelatedField(many=True, queryset=Habit.objects.all())
    class Meta:
        model=User
        fields=(
            'id',
            'username',
            'habits',
        )

