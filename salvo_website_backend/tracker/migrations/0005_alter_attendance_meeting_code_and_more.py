# Generated by Django 5.1.4 on 2024-12-11 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_meeting_date_alter_meeting_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='meeting_code',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='member_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2024, 12, 11, 16, 41, 3, 988071)),
        ),
    ]
