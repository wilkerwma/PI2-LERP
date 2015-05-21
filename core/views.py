from django.shortcuts import render
from django.shortcuts import render_to_response

#def home (request):


def home(request):
   
	return render(request,'index.html', {}) 

