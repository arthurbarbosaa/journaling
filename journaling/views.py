from django.shortcuts import render
from datetime import datetime
from calendar import monthrange

from .models import Journal,Header,Goal
#refatorar para ingles

ano_atual = datetime.now().year
mes_atual = datetime.now().month

nome_mes_atual = datetime.now().strftime("%B")
nome_dias_semana = []

num_dias_mes_atual = monthrange(ano_atual, mes_atual)[1]
for dia in range(1, num_dias_mes_atual + 1):
    data = datetime(ano_atual, mes_atual, dia)
    dia_semana = data.strftime("%d %A")
    nome_dias_semana.append(dia_semana)



def journal_list(request):
    print("Debugging: Entrou na minha_view")
    print(f"Debugging: variavel nome_mes_atual: {nome_mes_atual}")
    headers = Header.objects.all
    journals = Journal.objects.all


    return render(request, "journaling/journal_list.html", {
        "headers": headers,
        "journals": journals,
        "nome_mes_atual": nome_mes_atual,
        "nome_dias_semana": nome_dias_semana,
        
        })
