from django.shortcuts import render
from django.shortcuts import render_to_response
from core.models import *
from django.template import RequestContext
from django.contrib.auth import authenticate, login

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

    return render_to_response('index.html',{'state':state, 'username': username})

#def home(request):
#	return render_to_response('index.html')

def agenda(request):
	return render_to_response('agenda.html')

def contato(request):
	return render_to_response('contato.html')

def historico(request):
	return render_to_response( 'historico.html')

def sobre(request):
	return render_to_response('sobre.html')

def hist_limp(request):
  posts = Cleaning.objects.all().order_by("-collect_date")

  if request.method == 'POST':
      form = Cleaning(request.POST)
      if form.is_valid():
          form.save()
  else:
      form = Cleaning()
      variables = RequestContext(request, {'form':form, 'posts':posts})

  return render_to_response('hist_limp.html', variables)

def hist_turb(request):
  posts = History.objects.all().order_by("-collect_date")

  if request.method == 'POST':
      form = History(request.POST)
      if form.is_valid():
          form.save()
  else:
      form = History()
      variables = RequestContext(request, {'form':form, 'posts':posts})

  return render_to_response('hist_turb.html', variables)
