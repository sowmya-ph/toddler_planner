from django.shortcuts import render

# Create your views here.
def daily_schedule_list(request):
    return render(request, 'schedule_manager/daily_schedule.html', {})
