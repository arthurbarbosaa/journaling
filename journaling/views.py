from django.shortcuts import render
from .models import Journal

def journal_list(request):
    journals = Journal.objects.all

    return render(request, "journaling/journal_list.html", {"journals": journals})
