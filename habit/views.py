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
            return redirect(to='home')
    return render(request, 'base/add_habit.html', {'form':form})

def delete(request, pk):
    habit=get_object_or_404(Habit, pk=pk)
    if request.method=='POST':
        habit.delete()
        return redirect(to='home')
    return render (request, 'base/delete.html',{'habit':habit})


def habit_detail(request, pk):
    habit=get_object_or_404(Habit, pk=pk)
    result=Result.objects.all().filter(habit_id=habit.id)
    form=HabitForm()
    return render(request, 'base/details.html', {'habit':habit,'form':form,'result':result})

def update_daily(request, habit_pk, result_pk):
    habit=get_object_or_404(Habit,pk=habit_pk)
    result=get_object_or_404(Result,pk=result_pk)
    if request.method =='GET':
        form=ResultForm(request.POST,instance=result)
        if form.is_valid():
            form.save()
            return redirect(to='habit_detail',habit_pk=habit.pk)
        else:
            form=ResultForm(instance=result)
        return render(request,'update_daily.html',{'form':form,'habit':habit,'result':result})