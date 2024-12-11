from typing import Type
from maoObra import MaoObra
from produto import Produto

class Servico():
    def __init__(self, produto: Type[Produto], maoObra: Type[MaoObra]):
        self.__produto = produto
        self.__maoObra = maoObra

    def calcularValorServico(self):
        return self.__maoObra.obter_ValorTotal() + self.__produto.obter_ValorTotal()
    
    def mostrarServico(self):
        return (f"Produto: {self.__produto.obter_Tipo()}, Valor Total: {self.__produto.obter_ValorTotal()}\n"
                f"Mão de Obra: {self.__maoObra.obter_Descricao()}, Valor: {self.__maoObra.obter_ValorTotal()}")