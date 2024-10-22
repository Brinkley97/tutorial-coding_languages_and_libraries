from .models import Notes

from django.shortcuts import render

# Create your views here.

def list(request):
	all_notes = Notes.objects.all()
  # render the original request (via user/HTML request),
  # the name of the template (from [specific_app_folder]/[page_name].html), and 
  # empty brackets or can use Django template language to pass into something to render to [page_name].html
	return render(request, 'notes/notes_list.html', {'notes': all_notes})