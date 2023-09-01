from django.forms import ModelForm, TextInput, Textarea, Select
from .models import Produtos

class ProdutoForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['produto', 'cor', 'descricao']
        widgets = {
            'produto': TextInput(attrs={'class':'input'}),
            'cor': Select(attrs={'class':'select'}),
            'descricao': Textarea(attrs={'class':'textarea'}),
        }