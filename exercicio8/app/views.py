from django.shortcuts import render

from django.http import HttpResponse

def produto(request, categoria, nome):
    return HttpResponse(f"Produto: {nome.title()} | Categoria: {categoria.title()}")
