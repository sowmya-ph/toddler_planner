from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import date, time


class DailySchedule(models.Model):
    DAYS_OF_WEEK = (
            (0, 'Monday'),
            (1, 'Tuesday'),
            (2, 'Wednesday'),
            (3, 'Thursday'),
            (4, 'Friday'),
            (5, 'Saturday'),
            (6, 'Sunday'),
           )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    start_time = models.TimeField(default=time(hour=8, minute=0))
    end_time = models.TimeField(default=time(hour=16, minute=0))
    day = models.IntegerField(choices=DAYS_OF_WEEK)
    #weekid = models.ForeignKey(WeeklySchedule.weekid, on_delete = models.CASCADE)
    save_date = models.DateTimeField(default=timezone.now)

    def savedata(self):
        # todo: calculate weekid
        self.save_date = timezone.now()
        self.save()

    def __str__(self):
        return "{}:{}".format(self.date, self.DAYS_OF_WEEK[self.day][1])

#class WeeklySchedule(models.Model):
#    weekid = models.CharField(max_length=10)
#    hours_worked = models.
