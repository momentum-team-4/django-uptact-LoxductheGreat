# Generated by Django 3.1.1 on 2020-09-20 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0002_contact_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='note',
            field=models.DateTimeField(default='some string'),
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(default='some string', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]