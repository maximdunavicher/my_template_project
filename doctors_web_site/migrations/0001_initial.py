# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appointment_location', models.CharField(default=b'Home', max_length=1024)),
                ('appointment_date', models.DateTimeField(verbose_name=b'appointment date')),
                ('treatment_area', models.CharField(default=b'unknown', max_length=256)),
                ('other_comments', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('treatment_area', models.CharField(max_length=256)),
                ('treatment_time', models.DurationField(default=datetime.timedelta(0, 2400))),
                ('price', models.IntegerField(default=700)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('expertise', models.CharField(max_length=256)),
                ('person', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_birth', models.DateTimeField(verbose_name=b'date of birth')),
                ('phone_number', models.CharField(default=b'unknown', max_length=32)),
                ('registration_date', models.DateTimeField(verbose_name=b'registration date')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(to='doctors_web_site.Doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='person',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
