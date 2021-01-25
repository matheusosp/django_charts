from django.shortcuts import render
from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class IndexView(TemplateView):
    template_name = 'index.html'


class DadosJSONView(BaseLineChartView):

    def get_labels(self):
        labels= [
            "Janeiro","Fevereiro", "Março","Abril", "Maio","Junho",
            "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"
        ]
        return labels

    def get_providers(self):
        datasets = [
            "Teste 1",
            "Teste 2",
            "Teste 3",
            "Teste 4",
            "Teste 5",
            "Teste 6"
        ]
        return datasets

    def get_data(self):
        dados = []
        for c in range(6):
            for l in range(12):
                dado = [
                    randint(1, 200), #Janeiro
                    randint(1, 200), #Fevereiro
                    randint(1, 200), #Março
                    randint(1, 200), #Abril
                    randint(1, 200), #Maio
                    randint(1, 200), #Junho
                    randint(1, 200), #Julho
                    randint(1, 200), #Agosto
                    randint(1, 200), #Setembro
                    randint(1, 200), #Outubro
                    randint(1, 200), #Novembro
                    randint(1, 200), #Dezembro
                ]
            dados.append(dado)
        return dados