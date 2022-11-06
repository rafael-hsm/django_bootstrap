from django.shortcuts import render
from burger.models import Produto


def home(request):
    produtos = Produto.objects.all()
    context = {
        "produtos": produtos
    }
    return render(request, 'burger/home.html', context)


def detalhe_produto(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    context = { 
        'produto': produto
    }
    return render(request, 'burger/produto.html', context)
