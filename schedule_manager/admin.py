from django.contrib import admin
from .models import DailySchedule, WeeklySchedule

# Register your models here.
admin.site.register(DailySchedule)
admin.site.register(WeeklySchedule)

