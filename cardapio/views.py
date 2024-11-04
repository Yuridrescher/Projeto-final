from django.shortcuts import render
from .models import Cardapio
# Create your views here.

SEMANA = {
    2: "Segunda-Feira",
    3: "Terça-Feira",
    4: "Quarta-Feira",
    5: "Quinta-Feira",
    6: "Sexta-Feira",
}

def lanche(request, slug):
    cardapio = Cardapio.objects.get(slug=slug)
    context = {
        'semana':SEMANA[cardapio.semana],
        'imagem':cardapio.img.url,
        'titulo':cardapio.titulo,
        'descricao':cardapio.descricao,
    }

    return render(request, 'cardapio/cardapio-dia.html', context)

def index(request):
    return render(request, 'cardapio/index.html')
