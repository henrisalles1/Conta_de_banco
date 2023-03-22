from datetime import datetime

class Data:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.momento_cadastro.strftime('%d/%m/%Y %H:%M')

    @property
    def mes_cadastro(self):
        meses = ['','Janeiro', 'Favereiro', 'Março', 'Abril', 'Maio', 'Junho',
                 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        n_mes = self.momento_cadastro.month
        return meses[n_mes]

    @property
    def dia_semana_cadastro(self):
        dias = ['', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira',
                'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo'
                ]
        d_semana = self.momento_cadastro.weekday()
        return dias[d_semana]

    @property
    def hora_cadastro(self):
        hora = self.momento_cadastro.hour
        return hora

    @property
    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro
