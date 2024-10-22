from . import views

from django.urls import path

urlpatterns = [
	path('notes', views.list),
]