from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Users
# Create your views here.

def index(request):
    return HttpResponse("homepage")

def about(request):
    return HttpResponse("about sayfası")

def scoreBoard(request):
    
    return HttpResponse(Users.objects.all())


