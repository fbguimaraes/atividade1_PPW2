from django.shortcuts import render
from django.http import HttpResponse 

def download(request, nome, ext):
    return HttpResponse(f"Baixando: {nome}.{ext}")