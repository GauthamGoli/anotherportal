# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('myproject.myapp.views',
    url(r'^list/$', 'list', name='list'),
    url(r'^index/$', 'index', name='index'),
    url(r'^clouds/$', 'get_point_cloud_list', name='get_point_cloud_list'),
)
