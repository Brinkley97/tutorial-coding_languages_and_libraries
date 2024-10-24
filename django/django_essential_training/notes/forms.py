from django import forms # For more authentication

from .models import Notes

from django.core.exceptions import ValidationError

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control my-5'}),
        }
        labels = {
            'text': 'Write your thoughts here:'
        }

    # To specify notes that can and can NOT be added
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('Add "Django" to title')
        return title