__author__ = 'maxim'

from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^login_page/$', views.login_page, name='login_page'),
    url(r'^view_appointments/(?P<appointment_id>[0-9]+)$', views.detail, name='view_appointments'),
    url('^', include('django.contrib.auth.urls')),
]