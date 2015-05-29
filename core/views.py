from django.shortcuts import render
from django.shortcuts import render_to_response


#def home(request):
   # context = {'texto': 'Seu primeiro projeto Django no Linux/Ubuntu com Sublime Text 3'}
#    return render(request, 'index.html')

'''def home(request, url):
  #  m_list = MyModel.objects.filter(is_new=True)
    if url == 'home':
        template_name = 'index.html'
    elif url == 'agenda.html':
        template_name = 'agenda'
    return render(request, template_name)

'''
def home(request):
	return render_to_response('index.html')

def index(request):
    return render(request, 'index.html')

def agenda(request):
	return render(request, 'agenda.html',{}), 

def contato(request):
	return render(request, 'contato.html',{}),

def historico(request):
	return render(request, 'historico.html',{}),

def sobre(request):
	return render(request, 'sobre.html',{}),