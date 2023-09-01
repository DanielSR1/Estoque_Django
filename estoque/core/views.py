from django.shortcuts import render
# Create your views here.
def index(request):
    template_name = 'index.html'
    context = {
    'mensagem': 'Bem vindo à aplicação estoqueWeb'
    }
    return render(request, template_name, context)