from datetime import datetime

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

"""Learning purposes: Function-based views
# Create your views here.
def home(request):
    # render the original request, the name of the template, and empty brackets/Django template language
    return render(request, 'home/welcome.html', {'today': datetime.today})

@login_required(login_url='/admin')
def authorized(request):
    # render the original request, the name of the template, and empty brackets/Django template language
    return render(request, 'home/authorized.html', {})

"""

# Class-based views: https://www.linkedin.com/learning-login/share?account=76870426&forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fdjango-essential-training%2Fintroduction-to-django-class-based-views%3Ftrk%3Dshare_video_url%26shareId%3DxGUVf8a8QqeMF5b4gNVrvw%253D%253D
class HomeView(TemplateView):
	template_name = 'home/welcome.html'
	extra_context = {'today': datetime.today}
	
class AuthorizedView(LoginRequiredMixin, TemplateView):
	template_name = 'home/authorized.html'
	login_url = '/admin'