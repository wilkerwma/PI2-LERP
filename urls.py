"""lerp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from core.views import *


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','core.views.home', name = 'home'),
    url(r'^agenda$','core.views.agenda', name = 'agenda'),
    url(r'^index$','core.views.home'),
    url(r'^contato$','core.views.contato'),
    url(r'^historico$','core.views.historico', name = 'historico'),
    url(r'^hist_limp$','core.views.hist_limp'),
    url(r'^hist_turb$','core.views.hist_turb'),
    url(r'^sobre$','core.views.sobre'), 
    url(r'^ligar$','core.views.ligar',name='ligar'),
    url(r'^desligar$','core.views.desligar',name='desligar'),
    url(r'^update$','core.views.update',name='update'),
)