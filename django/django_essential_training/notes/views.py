from .models import Notes

from django.http import Http404
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

# Learning purposes: Function-based views
# Create your views here.
# def list(request):
# 	all_notes = Notes.objects.all()
#     # render the original request (via user/HTML request),
#     # the name of the template (from [specific_app_folder]/[page_name].html), and 
#     # empty brackets or can use Django template language to pass into something to render to [page_name].html
# 	return render(request, 'notes/notes_list.html', {'notes': all_notes})

# def detail(request, pk):
#     try:
#         note_details = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist.")
#     return render(request, 'notes/notes_details.html', {'note': note_details})



# Class-based views: https://www.linkedin.com/learning-login/share?account=76870426&forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fdjango-essential-training%2Fintroduction-to-django-class-based-views%3Ftrk%3Dshare_video_url%26shareId%3DxGUVf8a8QqeMF5b4gNVrvw%253D%253D

class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text'] # What fields to allow user to enter
    success_url = '/smart/notes' # Redirect user to all notes to show success

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_details.html"