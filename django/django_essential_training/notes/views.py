from .models import Notes
from .forms import NotesForm # For more authentication

from django.http import Http404
from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.http.response import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView


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

# CRUD

# C: Create
class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = '/smart/notes' # Redirect user to all notes to show successful creation
    form_class = NotesForm
    
    def form_valid(self, form):
        """New note auto belongs to user that is logged in
        
        Instead of title -> save() -> Database where we can't save bc no user is specified
        inject logged in user into object before saving to database with code below
        
        """
        self.object = form.save(commit=False) # Create object without saving to database
        self.object.user = self.request.user # Add user to object
        self.object.save() # Save to database
        return HttpResponseRedirect(self.get_success_url())

# R: Retrieve
class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/login" # Redirect to admin

    def get_queryset(self):
        """Get all notes related to a specific user

        Override base get_queryset() from https://ccbv.co.uk/projects/Django/5.0/django.views.generic.list/ListView/
        """
        return self.request.user.notes.all()

# R: Retrieve
class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_details.html" # So we aren't required to use Django's default file name, add own file name

# U: Update
class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    success_url = '/smart/notes' # Redirect user to all notes to show successful update
    form_class = NotesForm

# D: Delete
class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = "notes/notes_delete.html"