from django.contrib import admin
from .models import *

@admin.register(Document)
class DocumentModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'docs_file', 'date_posted',]

