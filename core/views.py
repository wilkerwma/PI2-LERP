from django.shortcuts import render
from django.shortcuts import render_to_response
from core.models import *
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as logout_auth
import urllib2
import xml.etree.ElementTree as ET


def home(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('index.html',{'state':state, 'username': username}, context_instance = RequestContext(request))

def logout(request):
  logout_auth(request)
  return render_to_response('logout.html')

def ligar (request):
  cleaning= Cleaning()
  cleaning.state_of_success =True
  time_of_cleaning = 0 
  cleaning.save()

  return render_to_response('index.html', context_instance = RequestContext(request) )

def desligar(request):
  
  return render_to_response('index.html', context_instance = RequestContext(request))  

def agenda(request):
	return render_to_response('agenda.html', context_instance = RequestContext(request))

def contato(request):
	return render_to_response('contato.html', context_instance = RequestContext(request))

def historico(request):
	return render_to_response( 'historico.html', context_instance = RequestContext(request))

def sobre(request):
	return render_to_response('sobre.html', context_instance = RequestContext(request))

def hist_limp(request):
  
  cleaning= Cleaning.objects.all()

  return render_to_response('hist_limp.html', {'cleaning': cleaning}, context_instance = RequestContext(request))

def hist_turb(request):
  history = History.objects.all().order_by("-collect_time")
  
  return render_to_response('hist_turb.html', {'history': history}, context_instance = RequestContext(request))


def update(request):
  
  file = urllib2.urlopen('https://script.google.com/macros/s/AKfycbzi0YFdb7ewTqv6_SJmICcITJ9Af_mRasmTaJQS8snG8ro9FQQ0/exec')
  tree = ET.parse(file)
  root = tree.getroot()
  history = History()

  for path in [ './ad1']:
    node = tree.find(path)
    history.sensor_low=int(node.text)
    print (history.sensor_low)
  for path in [ './ad2']:
    node = tree.find(path)
    history.sensor_mid=int(node.text)
    print (history.sensor_mid)
  for path in [ './ad3']:
    node = tree.find(path)
    history.sensor_high=int(node.text)
    print (history.sensor_high)
  for path in [ './ad4']:
    node = tree.find(path)
    history.sensor_floor=int(node.text)
    print (history.sensor_floor)

  history.save()
  history = History.objects.all().order_by("-collect_time")

  return render_to_response('hist_turb.html', {'history': history}, context_instance = RequestContext(request))

