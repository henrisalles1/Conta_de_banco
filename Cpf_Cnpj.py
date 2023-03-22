from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        doc_str = str(documento)
        digitos_a_remover = ['.', '/', '-']
        for x in range(len(digitos_a_remover)):
            doc_str = doc_str.replace(digitos_a_remover[x], '')
        if len(doc_str) == 11:
            return DocCpf(doc_str)
        elif len(doc_str) == 14:
            return DocCnpj(doc_str)
        else:
            raise ValueError('Documento Incorreto!')


class DocCpf:
    def __init__(self, cpf):
        if self.valida(cpf):
            self.cpf = cpf
        else:
            raise ValueError("Cpf inválido!")

    def __str__(self):
        return self.format()

    def valida(self, cpf):
        validador_cpf = CPF()
        return validador_cpf.validate(cpf)

    def format(self):
      mascara_cpf = CPF()
      return mascara_cpf.mask(self.cpf)


class DocCnpj:
    def __init__(self, cnpj):
        if self.cnpj_e_valido(cnpj):
            self.cnpj = cnpj
        else:
            raise ValueError('CNPJ inválido!')

    def __str__(self):
        return self.format_cnpj()

    def cnpj_e_valido(self, cnpj):
        validador_cnpj = CNPJ()
        return validador_cnpj.validate(cnpj)

    def format_cnpj(self):
        mascara_cnpj = CNPJ()
        return mascara_cnpj.mask(self.cnpj)
