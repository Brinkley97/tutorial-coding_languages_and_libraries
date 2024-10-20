from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    # render the original request, the name of the template, and empty brackets/Django template language
    return render(request, 'home/welcome.html', {'today': datetime.today})

@login_required(login_url='/admin')
def authorized(request):
    # render the original request, the name of the template, and empty brackets/Django template language
    return render(request, 'home/authorized.html', {})