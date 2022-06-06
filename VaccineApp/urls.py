from django.urls import re_path as url, path
from VaccineApp import views


urlpatterns=[
    url(r'^patient$', views.citizenApi),
    url(r'^patient/([0-9]+)$', views.citizenApi),
    path('Excel', views.save_file),
]