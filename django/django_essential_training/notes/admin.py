from . import models

from django.contrib import admin

# Without below, Notes class won't be add to the django admin interface
class NotesAdmin(admin.ModelAdmin):
    # pass # Don't want any additional configuration on this admin model
    list_display = ('title',) # In admin portal, go to Notes. Without, it'll say "Notes object (1)" and with, it'll say actual title of note

# Attach Notes model to NotesAdmin model (which is attached to the ModelAdmin)
admin.site.register(models.Notes, NotesAdmin)

