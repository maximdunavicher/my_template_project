from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Appointment, AppointmentPrice, Doctor
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


def logout_view(request):
    logout(request)
    return render(request, 'doctors_web_site/registration/login.html')


def check_login_view(request):
    username = request.POST['user']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render(request, 'doctors_web_site/index.html')
        else:
            return request(request, 'doctors_web_site/about.html')
    else:
        print ("user is None")


def signup_view(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    name = request.POST['name']
    last_name = request.POST['last_name']
    phone = request.POST['phone']
    birthday_date = request.POST['birthday']

    context = {
        "user": None
    }

    try:
        user = User.objects.create_user(username=username, email=email, password=password,
                                        last_name=last_name, first_name=name)

        user_profile = UserProfile(user=user,
                                   date_of_birth=birthday_date,
                                   phone_number=phone,
                                   registration_date=timezone.now())

        user_profile.save()

        context = {
            "user": user,
            "user_profile": user_profile
        }

        logger.debug("User created with the following data:\n"
                     "Username: {0}\n Email: {1}\n Password: {2}\n, Name: {3}\n Last_name:{4}\n Birthday:{5}".format(
                         username, email, password, name, last_name, birthday_date))

    except Exception as e:
        logger.debug("Failed to create the following user:\n"
                     "Username: {0}\n Email: {1}\n Password: {2}\n, Name: {3}\n Last_name:{4}\n Birthday:{5}".format(
                         username, email, password, name, last_name, birthday_date))

        logger.error(e)
        raise Http404("User was not created")

    user = authenticate(username=username, password=password)

    if user.is_active:
            login(request, user)

    return render(request, 'doctors_web_site/index.html', context)


def index(request):
    avalible_doctors = Doctor.objects.all()
    context = {'avalible_doctors': avalible_doctors}
    return render(request, 'doctors_web_site/index.html', context)


def about(request):
    return render(request, 'doctors_web_site/about.html')


def blog(request):
    return render(request, 'doctors_web_site/blog.html')


@login_required(login_url='doctors_web_site/registration/login.html')
def contact(request):
    return render(request, 'doctors_web_site/contact.html')


def login_page(request):
    if request.POST.get('login_button'):
        return check_login_view(request)

    elif request.POST.get('logout_button'):
        return logout_view(request)

    if request.POST.get('signup_button'):
        return signup_view(request)

    return render(request, 'doctors_web_site/registration/login.html')


def detail(request, appointment_id):
    all_appointments = Appointment.objects.all()
    all_prices = AppointmentPrice.objects.all()
    context = {"all_appointments": all_appointments, "all_prices": all_prices,
               "requested_appointment_id": appointment_id}

    return render(request, 'doctors_web_site/view_appointments.html', context)
