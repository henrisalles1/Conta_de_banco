from Cpf_Cnpj import Documento
from Telefone import Telefone
from Datas import Data
from Acesso_cep import BuscaEndereco

numero_conta = 0

class Conta:
    def __init__(self, titular, documento, limite):
        self._titular = str(titular)
        self._documento = Documento.cria_documento(str(documento))
        self._numero = numero_conta + 1
        self._saldo = 0
        self._limite = limite
        self._codigo_banco = "001"
        self._momento_cadastro = Data()
        print(f'Criando conta na memoria ...')


    def __str__(self):
        return f'Nome do Títular: {self._titular}\n' \
               f'Numero da Conta: {self._numero}\n' \
               f'Agencia: {self._codigo_banco}\n' \
               f'Saldo: {self._saldo}\n' \
               f'Limite: {self._limite}\n' \
               f'Para mais ações digite nomedaconta.help'

    @property
    def help(self):
        return '.extrato' \
               '.deposito(valor)' \
               '.saque(valor)' \
               '.transfere(valor,destino)' \
               '.saldo' \
               '.numero' \
               '.titular' \
               '.limite' \
               '.limite(novo_limite)' \
               '.codigo_banco' \
               '.momento_cadastro' \
               '.mostra_cep()' \
               '.muda_cep' \
               '.mostra_numero' \
               '.muda_telefone' \
               '.mostra_documento'

    @property
    def momento_cadastro(self):
        return self._momento_cadastro
    def mes_cadastro(self):
        return self._momento_cadastro.mes_cadastro
    def dia_da_semana_cadastro(self):
        return self._momento_cadastro.dia_semana_cadastro
    def hora_cadastro(self):
        return self._momento_cadastro.hora_cadastro
    def tempo_de_cadastro(self):
        return self._momento_cadastro.tempo_cadastro

    @property
    def mostra_telefone(self):
        return f'{self.telefone}'

    def muda_telefone(self, numero):
        self.telefone = Telefone(numero)
        print(f'Adicionado novo numero: {self.telefone}')

    def extrato(self):
        print('Saldo {} na conta de titular {}'.format(self._saldo, self._titular))

    def deposito(self, valor):
        self._saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self._saldo + self._limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saque(self, valor):
        if(self.__pode_sacar(valor)):
            self._saldo -= valor
        else:
            print("O valor do saque ultrapassa o limite de {}".format(self._limite))

    def transfere(self, valor, destino):
        if(valor <= self._saldo):
            self.saque(valor)
            destino.deposito(valor)
            print("Feita transferencia no valor de {}".format(valor))
        else:
            print("O valor {} é maior que seu saldo atual {}".format(valor, self._saldo))

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def nome_titular(self):
        return self._titular

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    def mostra_cep(self):
        bairro, cidade, uf = self.__cep.acessa_via_cep()
        print(f'{bairro}, {cidade}, {uf} - {self.__cep}')

    def mostra_documento(self):
        return self._documento

    def muda_cep(self, cep):
        self.__cep = BuscaEndereco(cep)
        bairro, cidade, uf = self.__cep.acessa_via_cep()
        print(f'Criado Novo CEP: {bairro}, {cidade}, {uf}.')




conta = Conta('Henrique','70.588.546/0001-90', 1000)
print(conta)