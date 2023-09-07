from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def vista1(request):
 return  HttpResponse("<h1> hola 1 </h1>")