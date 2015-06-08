from django.shortcuts import render
from django.shortcuts import render_to_response
from core.models import *
from django.template import RequestContext
#def home(request):
   # context = {'texto': 'Seu primeiro projeto Django no Linux/Ubuntu com Sublime Text 3'}
#    return render(request, 'index.html')


def home(request):
	return render_to_response('index.html')

def index(request):
    return render_to_response('index.html')

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
  return render_to_response('hist_turb.html')