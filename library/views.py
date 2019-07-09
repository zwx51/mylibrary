from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))