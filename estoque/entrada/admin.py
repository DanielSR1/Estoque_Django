from django.contrib import admin
from .models import Entradas


class EntradasAdmin(admin.ModelAdmin):
    list_display = [
        'produto',
        'preco',
        'quantidade',]

    
    
admin.site.register(Entradas, EntradasAdmin)


