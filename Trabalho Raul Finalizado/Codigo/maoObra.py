class MaoObra():
    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor  

    def informacaoServiço(self):
        return f"Servçio prestado\n{self.__descricao}\n\nValor total\n{self.__valor}"

    def obter_ValorTotal(self):
        return self.__valor  
    
    def obter_Descricao(self):
        return self.__descricao

    def definir_Descricao(self, descricao):
        self.__descricao = descricao


    def definir_Valor(self, valor):
        self.__valor = valor