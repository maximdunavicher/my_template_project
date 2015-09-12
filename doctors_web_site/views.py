from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Appointment, AppointmentPrice, Doctor
from django.contrib.auth import authenticate, login, logout
from django import forms


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
    birthday_date = request.POST['birthday']

    print username,email,password,name,last_name,birthday_date


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
