from . import views

from django.urls import path

# Learning purposes: Function-based views
# urlpatterns = [
# 	path('notes', views.list), # See all notes
#     path('notes/<int:pk>', views.detail), # See specific note
# ]


# Class-based urls: https://www.linkedin.com/learning-login/share?account=76870426&forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fdjango-essential-training%2Fintroduction-to-django-class-based-views%3Ftrk%3Dshare_video_url%26shareId%3DxGUVf8a8QqeMF5b4gNVrvw%253D%253D
urlpatterns = [
	path('notes', views.NotesListView.as_view(), name='notes_list'), # See all notes
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name='note_detail'), # See specific note
]