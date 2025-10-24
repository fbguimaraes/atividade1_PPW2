from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def data(request, ano, mes):
    if mes >= 1 and mes <=12:
        return HttpResponse(f"Ano: {ano}, Mês: {mes}")
    else:
        return HttpResponse("Insira um mês válido!!!")
    