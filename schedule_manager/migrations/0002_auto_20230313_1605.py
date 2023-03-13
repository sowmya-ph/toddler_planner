# Generated by Django 3.2.18 on 2023-03-13 23:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyschedule',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 3, 13, 23, 5, 45, 358776, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='dailyschedule',
            name='save_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 13, 23, 5, 45, 358811, tzinfo=utc)),
        ),
    ]