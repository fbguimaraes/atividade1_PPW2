from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Insira um nome na URL!!")

def saudacao(request, nome):
    return HttpResponse(f"Olá, {nome}!")

