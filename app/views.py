from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dashbord(request):
    return HttpResponse('Check the Models...')
