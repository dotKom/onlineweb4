# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('apps.inventory.dashboard.views',
    url(r'^$', 'index', name='inventory'),
    url(r'^item/(?P<pk>\d+)/$', 'details', name='details'),
)