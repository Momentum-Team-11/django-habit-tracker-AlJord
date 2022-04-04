from django import forms
from .models import Habit, Result


class HabitForm(forms.ModelForm):
    class Meta:
        model=Habit
        fields=('title','goal',)

class ResultForm(forms.ModelForm):
    class Meta:
        model=Result
        fields=('total',)