from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def vista2(request):
    return HttpResponse("<h1>Hola 2 </h1>")