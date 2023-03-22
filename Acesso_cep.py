import re
import requests

class BuscaEndereco:
    def __init__(self, CEP):
        cep = str(CEP)
        if self.cep_e_valido(cep):
            cep = cep.replace('-', '')
            self.cep = cep
        else:
            raise ValueError('CEP inválido!')

    def __str__(self):
        return self.format_cep

    @property
    def format_cep(self):
        return '{}-{}'.format(self.cep[:5],self.cep[5:])

    def cep_e_valido(self, cep):
        padrao_cep = re.compile('[0-9]{5}[-]?[0-9]{3}')
        achou_cep = re.findall(padrao_cep, cep)
        if achou_cep:
            return True
        else:
            return False

    def acessa_via_cep(self):
        url = 'https://viacep.com.br/ws/{}/json/'.format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )