"""habittracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from habit import views as habit_views
from api import views as api_views
from habit.models import Habit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path ('home', habit_views.home, name='home'),
    path('', habit_views.welcome, name='welcome'), #welcome page, user not registered
    path('habit/add', habit_views.add_habit, name='add_habit'),
    path ('habit/<int:pk>/delete', habit_views.delete, name='delete'),
    path('habit/<int:pk>/', habit_views.habit_detail, name='habit_detail'),
    path('habit/<int:habit_pk>/update_daily/', 
    habit_views.update_daily, name='update_daily'),
    path('habits/<int:pk>/', habit_views.edit_record, name='edit_record'),
    
    path('api-auth/', include('rest_framework.urls')),
    path("api/habit", api_views.HabitListView.as_view(), name="api_habit_list"),
    path('api/habit/records', api_views.ResultListView.as_view(), name='api_result_list'),
    path('api/habit/<int:pk>', api_views.HabitDetails.as_view(), name='habit_details'),
    ## path ('api/habit/update/<int:pk>/', api_views.HabitUpdate.as_view(), name='habit_update'),
    path('api/habit/delete/<int:pk>', api_views.HabitDetails.as_view(), name='habit_delete'),
    
    ]

