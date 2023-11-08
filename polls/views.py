from django.shortcuts import render 
from .models import Aluguel


def Carros (request):
    aluguels = Aluguel.objects.all()
    return render(request, 'polls/index.html', {'aluguels': aluguels})