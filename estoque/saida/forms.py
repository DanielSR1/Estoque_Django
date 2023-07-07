from django.forms import ModelForm
from .models import Saidas

class SaidasForm(ModelForm):
    class Meta:
        model = Saidas
        fields = ['produto', 'quantidade', 'preco']