from django.shortcuts import render

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list, name="list"),
    url(r'^album/(?P<slug>[-\w]+)$', views.detail,
        name="detail"),
]