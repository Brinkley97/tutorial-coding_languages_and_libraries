from .models import Notes

from django.http import Http404
from django.shortcuts import render

# Create your views here.
def list(request):
	all_notes = Notes.objects.all()
    # render the original request (via user/HTML request),
    # the name of the template (from [specific_app_folder]/[page_name].html), and 
    # empty brackets or can use Django template language to pass into something to render to [page_name].html
	return render(request, 'notes/notes_list.html', {'notes': all_notes})

def detail(request, pk):
    try:
        note_details = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist.")
    return render(request, 'notes/notes_details.html', {'note': note_details})