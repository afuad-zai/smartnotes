from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# just print something to show we reached this page
def home(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()})
