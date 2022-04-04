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

@login_required
def home(request):
    habit=Habit.objects.filter(user=request.user)
    return render(request, "base/home.html", {'habit': habit})

@login_required
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect(to='home')
    else:
        form = HabitForm()
    return render(request, 'base/add_habit.html',{'form':form})
    

@login_required
def delete(request, pk):
    habit=get_object_or_404(Habit, pk=pk)
    if request.method=='POST':
        habit.delete()
        return redirect(to='home')
    return render (request, 'base/delete.html',{'habit':habit})

@login_required
def habit_detail(request, pk):
    habit=get_object_or_404(Habit, pk=pk)
    result=Result.objects.all().filter(habit_id=habit.id)
    form=HabitForm()
    return render(request, 'base/details.html', {'habit':habit,'form':form,'result':result})

@login_required
def update_daily(request, habit_pk):
    habit=get_object_or_404(Habit, pk=habit_pk)
    if request.method=="GET":
        form=ResultForm()
    else:
        form=ResultForm(data=request.POST)
        if form.is_valid():
            result=form.save(commit=False)
            result.habit=habit
            result.save()
            return redirect(to='habit_detail', pk=habit.pk)
    return render(request, 'base/update_daily.html' ,{'form':form,'habit':habit})

@login_required
def edit_record(request, pk):
    record = Result.objects.filter(pk=pk).first()
    if request.method == 'GET':
        form = ResultForm(instance=record)
    else:
        form = ResultForm(request.POST, instance=record)
    if form.is_valid():
        form.save()
        return redirect(to='detail', pk=record.habit.pk)
    return render(request, 'edit_record.html', {'form': form, 'result': result})