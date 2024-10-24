from . import views

from django.urls import path

"""Learning purposes: Function-based views
urlpatterns = [
    path('home', views.home),
    path('authorized', views.authorized)
]
"""

# Class-based views: https://www.linkedin.com/learning-login/share?account=76870426&forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fdjango-essential-training%2Fintroduction-to-django-class-based-views%3Ftrk%3Dshare_video_url%26shareId%3DxGUVf8a8QqeMF5b4gNVrvw%253D%253D
urlpatterns = [
    path('home', views.HomeView.as_view(), name='home.page'),
    path('authorized', views.AuthorizedView.as_view())
]