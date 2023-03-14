from django.shortcuts import render
from .models import DailySchedule
from datetime import datetime
import pprint

# Create your views here.
def daily_schedule_list(request):
    # Fetch all schedule objects from the model, reverse chronologically ordered
    schedules = DailySchedule.objects.order_by('-date')
    # Construct a dictionary grouped by month-year
    monthly_grouping = {}
    for schedule in schedules:
        month_year = schedule.date.strftime('%b')  + " " + str(schedule.date.year) 
        if month_year not in monthly_grouping:
            monthly_grouping[month_year] = [schedule]
        else:
            monthly_grouping[month_year].append(schedule)

    context = {"monthly_grouping": monthly_grouping}
    return render(request, 'schedule_manager/daily_schedule.html', context)
