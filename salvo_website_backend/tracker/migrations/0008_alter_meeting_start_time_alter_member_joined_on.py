# Generated by Django 5.1.4 on 2024-12-13 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_alter_meeting_start_time_alter_member_joined_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2024, 12, 13, 16, 33, 6, 481286)),
        ),
        migrations.AlterField(
            model_name='member',
            name='joined_on',
            field=models.DateField(default=datetime.datetime(2024, 12, 13, 11, 3, 6, 481286, tzinfo=datetime.timezone.utc)),
        ),
    ]
