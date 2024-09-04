from django.shortcuts import render
from django.http import HttpResponse

def home_gepetosa(request):
    return render(
        request, 
        'index_gepetoso.html', 
        {
            "var_alguma_coisa": "Texto do attr var_alguma_coisa coloque aqui o conteudo dinamico"
        }
    )