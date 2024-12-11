from veiculo import Veiculo
from servico import Servico
from cliente import Cliente
from datetime import date
from typing import Type

class Orcamento:
    def __init__(self, codigo, data_entrada: date, veiculo: Veiculo, servico: Servico, cliente: Cliente):
        self.__codigo = codigo
        self.__data_entrada = data_entrada
        self.__veiculo = veiculo
        self.__servico = servico
        self.__cliente = cliente

    def juntarInfo(self):
        # Organizando as informações em um formato mais legível e bonito
        veiculo_info = (
            f"Nome: {self.__veiculo.obter_Nome()}\n"
            f"Quilometragem: {self.__veiculo.obter_Quilometragem()} km\n"
            f"Montadora: {self.__veiculo.obter_Montadora()}\n"
            f"Placa: {self.__veiculo.obter_Placa()}\n"
            f"Ano: {self.__veiculo.obter_Ano()}\n"
            f"Chassi: {self.__veiculo.obter_Chassi()}\n"
            f"Frota: {self.__veiculo.obter_Frota()}\n"
        )

        cliente_info = (
            f"Nome: {self.__cliente.obter_Nome()}\n"
            f"Telefone: {self.__cliente.obter_Telefone()}\n"
            f"Seguradora: {self.__cliente.obter_Seguradora()}\n"
        )

        servico_info = f"Serviço: {self.__servico.mostrarServico()}\n"
        
        # Retornando todas as informações de forma organizada
        return (
            f"===== ORÇAMENTO =====\n"
            f"Código: {self.__codigo}\n"
            f"Data de Entrada: {self.__data_entrada}\n\n"
            f"--- VEÍCULO ---\n"
            f"{veiculo_info}\n"
            f"--- SERVIÇO ---\n"
            f"{servico_info}\n"
            f"--- CLIENTE ---\n"
            f"{cliente_info}\n"
            "====================="
        )

    def obter_Codigo(self):
        return self.__codigo

    def definirCodigo(self, codigo):
        self.__codigo = codigo

    def obter_Data(self):
        return self.__data_entrada

    def definir_Data(self, data_entrada):
        self.__data_entrada = data_entrada

    def obter_Veiculo(self): 
        return self.__veiculo

    def obter_Servico(self): 
        return self.__servico

    def obter_Cliente(self):
        return self.__cliente

    def definir_Veiculo(self, veiculo):
        self.__veiculo = veiculo

    def definir_Servico(self, servico):
        self.__servico = servico

    def definir_Cliente(self, cliente):
        self.__cliente = cliente