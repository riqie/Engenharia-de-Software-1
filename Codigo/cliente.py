class Cliente:
    def __init__(self, nome, telefone, seguradora):
        self.__nome = nome
        self.__telefone = telefone
        self.__seguradora = seguradora

 
    def obter_Nome(self):
        return self.__nome

    def definir_Nome(self, nome):
        self.__nome = nome

    def obter_Telefone(self):
        return self.__telefone

    def definir_Telefone(self, telefone):
        self.__telefone = telefone

    def obter_Seguradora(self):
        return self.__seguradora

    def definir_Seguradora(self, seguradora):
        self.__seguradora = seguradora

    def __str__(self):
        return (f"Nome: {self.__nome}\n"
                f"Telefone: {self.__telefone}\n"
                f"Seguradora: {self.__seguradora}")