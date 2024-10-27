from datetime import datetime

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
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
	
class LoginInterfaceView(LoginView):
	template_name = 'home/login.html'
      
class LogoutInterfaceView(LogoutView):
	template_name = 'home/logout.html'


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'
    
    def get(self, request, *args, **kwargs):
        """User login
        
        If user is already authenticated, go to list of
        If user is not already authenticated, do so

        """
        
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)

