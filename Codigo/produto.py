class Produto():
    def __init__(self, tipo, valor, quantidade):
        self.__tipo = tipo
        self.__valor = valor
        self.__quantidade = quantidade

    def informacaoServiço(self):
        return f"Produto utilizado\n{self.__tipo}\n\nQuantidade\n{self.__quantidade}\n\nValor total\n{self.__valor}"

    def obter_ValorTotal(self):
        return self.__valor * self.__quantidade
    
    def obter_Tipo(self):
        return self.__tipo
    
    def definir_Tipo(self, new_tipo):
        self.__tipo = new_tipo

    def definir_Valor(self, new_valor):
        self.__valor = new_valor

    def obter_Quantidade(self):
        return self.__quantidade
    
    def definir_Quantidade(self, new_quantidade):
        self.__quantidade = new_quantidade