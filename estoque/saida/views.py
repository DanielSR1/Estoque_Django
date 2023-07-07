from django.shortcuts import render, redirect
from .models import Saidas
from .forms import SaidasForm
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
# Create your views here.
def list_saida(request):
    saidas = Saidas.objects.all()
    template_name = 'list_saida.html'
    context = {
    'saidas': saidas,
    }
    return render(request, template_name, context)

def new_saida(request):
    if request.method == 'POST':
        form = SaidasForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['produto'].quantidade < form.cleaned_data['quantidade']:
                messages.error(request,f'Por favor insira um valor até {form.cleaned_data["produto"].quantidade }')
                return redirect('saida:new_saida')
            form.save(commit=False)
            form.cleaned_data['produto'].preco = form.cleaned_data['preco']
            form.cleaned_data['produto'].quantidade = form.cleaned_data['produto'].quantidade - form.cleaned_data['quantidade']
            form.cleaned_data['produto'].save_base()
            form.save()
        
            return redirect('saida:list_saida')
    else:
        template_name = 'new_saida.html'
        context = {
        'form': SaidasForm(),
        }
        return render(request, template_name, context)

def update_saida(request, pk):
    saida = Saidas.objects.get(pk=pk)
    quantidade_anterior = saida.quantidade
    if request.method == 'POST':
        form = SaidasForm(request.POST, instance=saida)
        if form.is_valid():
            produto = form.cleaned_data['produto']
            quantidade_atual = form.cleaned_data['quantidade']
            diferenca = quantidade_atual - quantidade_anterior
            produto.quantidade -= diferenca
            produto.save()
            form.save()
            return redirect('saida:list_saida')
    else:
        template_name = 'update_saida.html'
        context = {
            'form': SaidasForm(instance=saida),
            'pk': pk,
        }
        return render(request, template_name, context)
    
def delete_saida(request, pk):
    saida = Saidas.objects.get(pk=pk)
    saida.produto.quantidade = saida.produto.quantidade - saida.quantidade
    saida.produto.save()
    saida.delete()
    
    return redirect('saida:list_saida')
