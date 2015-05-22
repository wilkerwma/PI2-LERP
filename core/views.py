from django.shortcuts import render
from django.shortcuts import render_to_response


def home(request):
    context = {'texto': 'Seu primeiro projeto Django no Linux/Ubuntu com Sublime Text 3'}
    return render(request, 'index.html', context)
