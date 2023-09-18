from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView

from .models import Notes

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    # we can omit code below because our template is folowing the correct convention
    #template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"