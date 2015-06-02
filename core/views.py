from django.shortcuts import render
from django.shortcuts import render_to_response


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