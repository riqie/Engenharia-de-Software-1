class Funcionario:
    def __init__(self, nome: str, cpf: str, salario: float, cargo: str):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo
        
    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Salário: R${self.salario}, Cargo: {self.cargo}"
