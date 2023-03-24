from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import date, time
from functools import partial
from math import floor

DAYS_OF_WEEK = (
            (0, 'Monday'),
            (1, 'Tuesday'),
            (2, 'Wednesday'),
            (3, 'Thursday'),
            (4, 'Friday'),
            (5, 'Saturday'),
            (6, 'Sunday'),
           )

class Util():
    @classmethod
    def addDays(type_arg, num_days):
        return timezone.now() + timezone.timedelta(days=num_days)

class WeeklySchedule(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #hours_worked = models.IntegerField()
    # todo: pass default date for each day
    day1 = models.ForeignKey('schedule_manager.DailySchedule', on_delete = models.SET_NULL, null = True, related_name='day1')
    day2 = models.ForeignKey('schedule_manager.DailySchedule', on_delete = models.SET_NULL, null = True, related_name='day2' )
    day3 = models.ForeignKey('schedule_manager.DailySchedule', on_delete = models.SET_NULL, null = True, related_name='day3')
    day4 = models.ForeignKey('schedule_manager.DailySchedule', on_delete = models.SET_NULL, null = True, related_name='day4')
    day5 = models.ForeignKey('schedule_manager.DailySchedule', on_delete = models.SET_NULL, null = True, related_name='day5')
    day6 = models.ForeignKey('schedule_manager.DailySchedule', on_delete = models.SET_NULL, null = True, related_name='day6')
    day7 = models.ForeignKey('schedule_manager.DailySchedule', on_delete = models.SET_NULL, null = True, related_name='day7')

    #day1_date = models.DateField(default=timezone.now)
    #day2_date = models.DateField(default=partial(Util.addDays, num_days=1))
    #day3_date = models.DateField(default=partial(Util.addDays, num_days=2))
    #day4_date = models.DateField(default=partial(Util.addDays, num_days=3))
    #day5_date = models.DateField(default=partial(Util.addDays, num_days=4))
    #day6_date = models.DateField(default=partial(Util.addDays, num_days=5))
    #day7_date = models.DateField(default=partial(Util.addDays, num_days=6))

    @property
    def hours_worked(self):
        #self.day1.aggregate(Sum('hours_worked'))
        return self.day1.hours_worked + self.day2.hours_worked  + self.day3.hours_worked  + self.day4.hours_worked  + self.day5.hours_worked  + self.day6.hours_worked  + self.day7.hours_worked 
        #[self.day1, self.day2, self.day3, self.day4, self.day5, self.day6, self.day7].aggregate(Sum('hours_worked'))

    def savedata(self):
        self.save()

    def __str__(self):
        return "{} to {}".format(self.day1.date, self.day7.date)

class DailySchedule(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    start_time = models.TimeField(default=time(hour=8, minute=0))
    end_time = models.TimeField(default=time(hour=16, minute=0))
    day = models.IntegerField(choices=DAYS_OF_WEEK)
    save_date = models.DateTimeField(default=timezone.now)

    @property 
    def hours_worked(self):
        end_minutes = self.end_time.hour*60 + self.end_time.minute
        start_minutes = self. start_time.hour*60 + self.start_time.minute
        return floor((end_minutes - start_minutes) / 60)

    def savedata(self):
        self.save_date = timezone.now()
        self.save()

    def __str__(self):
        return "{}".format(self.date)
        #return "{}:{}".format(self.date, DAYS_OF_WEEK[self.day][1])
    


