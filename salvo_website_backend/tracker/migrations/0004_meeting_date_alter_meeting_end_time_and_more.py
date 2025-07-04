# Generated by Django 5.1.4 on 2024-12-11 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_alter_attendance_duration_alter_meeting_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 12, 11, 13, 23, 29, 702863)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meeting',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2024, 12, 11, 13, 23, 12, 227935)),
        ),
    ]
