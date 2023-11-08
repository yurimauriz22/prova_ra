from django.shortcuts import render 
from .models import Carro


def Carros (request):
    carro = Carro.objects.all()
    return render(request, 'polls/index.html', {'carro': carro})