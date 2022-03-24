from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Habit, Result, User
from .forms import HabitForm, ResultForm


def welcome(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'base/welcome.html')

def home(request):
    habit=Habit.objects.all()
    return render(request, "base/home.html", {'habit': habit})

def add_habit(request):
    if request.method == 'GET':
        form=HabitForm()
    else:
        form=HabitForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='add_habit')
    return render(request, 'base/add_habit.html', {'form':form})