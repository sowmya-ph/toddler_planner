from django.urls import path
from . import views

urlpatterns = [
    path('', views.daily_schedule_list, name='daily_schedule_list'),
]
