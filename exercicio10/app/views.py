from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Lista de posts do blog")

def post(request, ano, slug):
    return HttpResponse(f"Post de {ano}: {slug.replace('-', ' ').title()}")

def autor(request, nome):
    return HttpResponse(f"Posts do autor: {nome.title()}")
