import re

class Telefone:
    def __init__(self, telefone):
        self.telefone = self.tira_espaco_telefone(telefone)
        if self.valida_telefone(self.telefone):
            self.numero = telefone
        else:
            raise ValueError('Numero de Telefone Incorreto')

    def __str__(self):
        return self.format_numero

    def tira_espaco_telefone(self,numero):
        if type(numero) == str:
            return numero.strip()
        else:
            return ''

    @property
    def format_numero(self):
        digitos_a_retirar = ['+', '(', ')', '-']
        for x in range(len(digitos_a_retirar)):
            self.numero = self.numero.replace(digitos_a_retirar[x], '')
        if len(self.numero) == 13:
            return '+{}({}){}-{}'.format(
                self.numero[:2],
                self.numero[2:4],
                self.numero[4:12],
                self.numero[12:]
            )

    def valida_telefone(self, telefone):
        padrao_numero = re.compile('(([+][0-9]{2})?([(][0-9]{2}[)]))|([0-9]{2})[0-9]{4,5}[-]?[0-9]{4}')
        numero = re.findall(padrao_numero, telefone)
        if numero:
            return True
        else:
            return False




