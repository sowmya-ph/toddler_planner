from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import DailySchedule, WeeklySchedule
from .forms import DailyScheduleForm, WeeklyScheduleForm, DailyScheduleFormSetHelper
import datetime
import pprint
from django.views import generic
from django.views.generic.edit import View, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import formset_factory

class WeeklyScheduleView(generic.ListView):
    model = WeeklySchedule

class WeeklyScheduleCreate(View):
    template = 'schedule_manager/weeklyschedule_form.html'
    success_url = reverse_lazy('schedule_manager:weeklyschedule_list')

    def get(self, request):
        DayFormSet = formset_factory(DailyScheduleForm, extra=7, max_num=7, absolute_max=7)
        dayforms = DayFormSet()
        helper = DailyScheduleFormSetHelper()
        #print(dayforms.as_table())
        ctx = {'dayforms': dayforms, 'helper': helper}
        return render(request, self.template, ctx)

    def post(self, request):
        print(str(request.POST))
        DayFormSet = formset_factory(DailyScheduleForm)
        dayforms = DayFormSet(request.POST)
        
        daydata = []
        print("saving..")
        for form in dayforms:
            daydata.append(form.save())

        #TODO: Non-atomic save - change to only save all objects only after all validations are done
        data = {"day1": daydata[0], "day2":daydata[1], "day3":daydata[2], "day4":daydata[3], "day5":daydata[4], "day6":daydata[5], "day7":daydata[6]}
        weeklyform = WeeklyScheduleForm(data)
        if not dayforms.is_valid() or not weeklyform.is_valid():
            print("error while validating forms")
            print("errors = " + str(weeklyform.errors))
            print("non field errors = " + str(weeklyform.non_field_errors))
            ctx = {'dayforms': dayforms, 'weeklyform':weeklyform}
            return render(request, self.template, ctx)

        weeklyform.save()
        return redirect(self.success_url)

class WeeklyScheduleUpdate(View):
    model=WeeklySchedule
    #exclude=["user"]
    success_url=reverse_lazy('schedule_manager:weeklyschedule_list')

class WeeklyScheduleDelete(DeleteView):
    #TODO: delete day entries when week is deleted
    model=WeeklySchedule
    success_url=reverse_lazy('schedule_manager:weeklyschedule_list')


class Daily_schedule_generic(generic.ListView):
    model = DailySchedule

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
