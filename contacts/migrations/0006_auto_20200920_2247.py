# Generated by Django 3.1.1 on 2020-09-20 22:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20200920_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='note',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
