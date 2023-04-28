from django.shortcuts import HttpResponse, render
from carro.carro import Carro 

def inicio(request):
    carro=Carro(request)
    return render(request, "MunalaApp/inicio.html")









