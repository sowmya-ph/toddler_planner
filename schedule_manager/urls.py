from django.urls import path
from . import views

app_name="schedule_manager"
urlpatterns = [
    path('', views.WeeklyScheduleView.as_view(), name='weeklyschedule_list'),
    path('create', views.WeeklyScheduleCreate.as_view(), name='weeklyschedule_create'),
    path('schedule<int:pk>/update', views.WeeklyScheduleUpdate.as_view(), name='weeklyschedule_update'),
    path('schedule/<int:pk>delete', views.WeeklyScheduleDelete.as_view(), name='weeklyschedule_delete'),
    path('generic', views.Daily_schedule_generic.as_view(), name='daily_schedule_generic'),
]
