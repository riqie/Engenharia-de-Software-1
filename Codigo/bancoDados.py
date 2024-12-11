class BancoDeDados:
    contagem_itens = {
        'itens': 0,
        'funcionarios': 0,
        'orcamentos': 0
    }

    def __init__(self):
        self.itens = {}
        self.funcionarios = {}
        self.orcamentos = {}

    def exibir_contagem(self):
        return BancoDeDados.contagem_itens