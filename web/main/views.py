from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "index.html", {"error": "Bad username or password!"})
def login(request):
    return render(request, "login.html", {"error": "Bad username or password!"})
