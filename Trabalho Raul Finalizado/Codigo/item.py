from abc import abstractmethod

class Item:
    def __init__(self, nome: str, codigo: str, quantidade: int):
        self.nome = nome
        self.codigo = f"{self.nome[:3].upper()}-{codigo}"
        self.quantidade = quantidade

    @abstractmethod
    def obter_detalhes(self):
        pass