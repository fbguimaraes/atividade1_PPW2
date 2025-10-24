from django.shortcuts import render
from django.http import HttpResponse

def artigo(request, slug):
    return HttpResponse(f"Título do artigo: {slug.replace('-', ' ').title()}")