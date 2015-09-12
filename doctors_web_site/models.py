from datetime import timedelta
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateTimeField('date of birth')
    phone_number = models.CharField(max_length=32, default="unknown")
    registration_date = models.DateTimeField('registration date')

    def __unicode__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)


class AppointmentPrice(models.Model):

    treatment_area = models.CharField(max_length=256)
    treatment_time = models.DurationField(default=timedelta(minutes=40))
    price = models.IntegerField(default=700)

    def __unicode__(self):
        return "Price:{0}\ntime:{1} minutes\narea:{2}".format(self.price, self.treatment_time, self.treatment_area)


class Doctor(models.Model):
    person = models.OneToOneField(User, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=256)

    def __unicode__(self):
        return "Doctor {0} {1}".format(self.person.first_name, self.person.last_name)


class Appointment(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_location = models.CharField(max_length=1024, default='Home')
    appointment_date = models.DateTimeField('appointment date')
    treatment_area = models.CharField(max_length=256, default='unknown')
    other_comments = models.CharField(max_length=1024)

    def __unicode__(self):
        return "Doctor {2} {3}\nPatient {0} {1}".format(self.person.first_name, self.person.last_name,
                                                        self.doctor.person.first_name, self.doctor.person.last_name)

