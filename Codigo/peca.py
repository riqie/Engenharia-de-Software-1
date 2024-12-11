from item import *

class ValidadorPeca:
    @staticmethod
    def validar_nome(nome):
        if not isinstance(nome, str):
            raise ValueError("O nome deve ser uma string.")

    @staticmethod
    def validar_codigo(codigo):
        if not isinstance(codigo, str):
            raise ValueError("O código deve ser uma string.")

    @staticmethod
    def validar_quantidade(quantidade):
        if not isinstance(quantidade, int) or quantidade < 0:
            raise ValueError("A quantidade deve ser um número inteiro não negativo.")

    @staticmethod
    def validar_especificacao(especificacao):
        if not isinstance(especificacao, str):
            raise ValueError("A especificação deve ser uma string.")

class Peca(Item):
    def __init__(self, nome: str, codigo: str, quantidade: int, especificacao: str):
        super().__init__(nome, codigo, quantidade)
        self._especificacao = especificacao
        self._codigo = codigo

    def obter_detalhes(self):
            return f"Especificação: {self.especificacao}"

    def definir_especificacao(self, valor):
        ValidadorPeca.validar_especificacao(valor)
        self._especificacao = valor

    def obter_codigo(self):
        return self._codigo

    def definir_codigo(self, valor):
        ValidadorPeca.validar_codigo(valor)
        self._codigo = valor

    def __str__(self):
        return f"Peça: {self.nome}, Código: {self._codigo}, Quantidade: {self.quantidade}, Especificação: {self._especificacao}"