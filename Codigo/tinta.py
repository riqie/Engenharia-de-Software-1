from item import *

class ValidadorTinta:
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
    def validar_cor(cor):
        if not isinstance(cor, str):
            raise ValueError("A cor deve ser uma string.")

    @staticmethod
    def validar_volume(volume):
        if not isinstance(volume, (int, float)) or volume <= 0:
            raise ValueError("O volume deve ser um número positivo.")

class Tinta(Item):
    def __init__(self, nome: str, codigo: str, quantidade: int, cor: str, volume: float):
        super().__init__(nome, codigo, quantidade)
        self._cor = cor
        self._volume = volume

    def obter_detalhes(self):
        return f"Cor: {self.cor}, Volume: {self.volume}ml"

    def obter_cor(self):
        return self._cor

    def definir_cor(self, valor):
        ValidadorTinta.validar_cor(valor)
        self._cor = valor

    def obter_volume(self):
        return self._volume

    def definir_volume(self, valor):
        ValidadorTinta.validar_volume(valor)
        self._volume = valor

    def __str__(self):
        return f"Tinta: {self.nome}, Código: {self.codigo}, Quantidade: {self.quantidade}, Cor: {self._cor}, Volume: {self._volume}ml"