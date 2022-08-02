from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name':'Miguel Sosa Villegas'})

def about(request):
    return render(request, 'about.html')