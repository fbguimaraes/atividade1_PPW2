from django.shortcuts import render
from django.http import HttpResponse

def soma(request, a, b):
    return HttpResponse(f"Resultado: {a + b}")
