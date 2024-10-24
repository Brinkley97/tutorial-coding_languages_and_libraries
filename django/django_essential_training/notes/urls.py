from . import views

from django.urls import path

urlpatterns = [
	path('notes', views.list), # See all notes
    path('notes/<int:pk>', views.detail), # See specific note
]