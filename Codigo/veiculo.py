class Veiculo:
    def __init__(self, nome, quilometragem, montadora, placa, ano, chassi, frota):
        self.__nome = nome
        self.__quilometragem = quilometragem
        self.__montadora = montadora
        self.__placa = placa
        self.__ano = ano
        self.__chassi = chassi
        self.__frota = frota

  
    def obter_Nome(self):
        return self.__nome

    def definir_Nome(self, nome):
        self.__nome = nome

    def obter_Quilometragem(self):
        return self.__quilometragem

    def definir_Quilometragem(self, quilometragem):
        self.__quilometragem = quilometragem

    def obter_Montadora(self):
        return self.__montadora

    def definir_Montadora(self, montadora):
        self.__montadora = montadora

    def obter_Placa(self):
        return self.__placa

    def definir_Placa(self, placa):
        self.__placa = placa

    def obter_Ano(self):
        return self.__ano

    def definir_Ano(self, ano):
        self.__ano = ano

    def obter_Chassi(self):
        return self.__chassi

    def definir_Chassi(self, chassi):
        self.__chassi = chassi

    def obter_Frota(self):
        return self.__frota

    def definir_Frota(self, frota):
        self.__frota = frota

    
    def __str__(self):
        return (f"Veículo: {self.__nome}\n"
                f"Quilometragem: {self.__quilometragem} km\n"
                f"Montadora: {self.__montadora}\n"
                f"Placa: {self.__placa}\n"
                f"Ano: {self.__ano}\n"
                f"Chassi: {self.__chassi}\n"
                f"Frota: {self.__frota}")