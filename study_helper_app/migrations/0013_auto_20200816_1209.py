# Generated by Django 3.1 on 2020-08-16 12:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('study_helper_app', '0012_auto_20200816_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='repeat_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 16, 12, 9, 12, 880640, tzinfo=utc), verbose_name='Дата Повторения'),
        ),
    ]
