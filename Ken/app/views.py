from django.shortcuts import render_to_response
# Create your views here.
from .models import Information

def index(request):
	Informations = Information.objects.all()
	return render_to_response('app/menu.html',locals())
