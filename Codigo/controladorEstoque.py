from bancoDados import *
from tinta import *
from ferramenta import *
from peca import *
from funcionario import *
from validarentrada import *

class ControladorEstoque:
    def __init__(self, banco_de_dados: BancoDeDados):
        self.banco_de_dados = banco_de_dados

    def menuGerenciamento(self):
        while True:
            print("\n===== Menu de Gerenciamento =====")
            print("1. Cadastrar item")
            print("2. Cadastrar funcionário")
            print("3. Remover item")
            print("4. Remover funcionário")
            print("5. Editar item ou funcionário")
            print("6. Exibir itens cadastrados")
            print("7. Exibir funcionários cadastrados")
            print("8. Voltar")

            escolha = input("Escolha uma opção: ")
            
            if escolha == '1':
                # Cadastrar item
                while True:
                    print("Qual tipo de item deseja cadastrar no estoque?\n[1] - Ferramenta\n[2] - Tinta\n[3] - Peça")
                    resp = int(input(": "))
                    if resp == 1:
                        nome_item = input("Nome da ferramenta: ")
                        codigo_item = input("Digite o número da ferramenta: ")
                        quantidade_item = validar_int("Quantidade a serem adicionadas: ")
                        ferramenta = Ferramenta(nome_item, codigo_item, quantidade_item)
                        self.cadastrarItem(ferramenta)
                        print(f"Ferramenta - {codigo_item} cadastrada com sucesso!")
                        break

                    elif resp == 2:
                        nome_item = input("Nome da tinta: ")
                        codigo_item = input("Digite o número da tinta: ")
                        quantidade_item = validar_int("Quantidade a serem adicionadas: ")
                        cor_item = input("Digite a cor da tinta: ")
                        volume_item = validar_float("Digite o volume da tinta (ml): ")
                        tinta = Tinta(nome_item, codigo_item, quantidade_item, cor_item, volume_item)
                        self.cadastrarItem(tinta)
                        print(f"Tinta - {codigo_item} cadastrada com sucesso!")
                        break

                    elif resp == 3:
                        nome_item = input("Nome da peça: ")
                        codigo_item = input("Digite o número da peça: ")
                        quantidade_item = validar_int("Quantidade a serem adicionadas: ")
                        espcificacao_item = input("Digite a especificação da peça: ")
                        peca = Peca(nome_item, codigo_item, quantidade_item, espcificacao_item)
                        self.cadastrarItem(peca)
                        print(f"Peça - {codigo_item} cadastrada com sucesso!")
                        break

                    else:
                        print("Opção inválida, tente novamente.")

            elif escolha == '2':
                # Cadastrar funcionário
                nome_funcionario = input("Digite o nome do funcionário: ")
                cpf_funcionario = input("Digite o CPF do funcionário: ")
                salario_funcionario = validar_float("Digite o salário do funcionário: ")
                cargo_funcionario = input("Digite o cargo do funcionário: ")

                funcionario = Funcionario(nome_funcionario, cpf_funcionario, salario_funcionario, cargo_funcionario)
                self.cadastrarFuncionario(funcionario)
                print(f"Funcionário {nome_funcionario} cadastrado com sucesso!")

            elif escolha == '3':
                # Remover item
                self.exibirItens()
                codigo_item = input("Digite o código do item a ser removido: ")
                self.removerItem(codigo_item)

            elif escolha == '4':
                # Remover funcionário
                self.exibirFuncionarios()
                codigo_funcionario = input("Digite o cpf do fucionário a ser removido: ")
                self.removerFuncionario(codigo_funcionario)

            elif escolha == '5':
                # Editar item ou funcionário
                tipo_objeto = input("Você deseja editar um 'item' ou um 'funcionario'? ").lower()
                if tipo_objeto == 'item':
                    self.exibirItens()
                    codigo_item = input("Digite o código do item a ser editado: ")
                    self.editarObjeto(codigo_item, tipo_objeto)

                elif tipo_objeto == 'funcionario':
                    self.exibirFuncionarios()
                    cpf_funcionario = input("Digite o CPF do funcionário a ser editado: ")
                    self.editarObjeto(cpf_funcionario, tipo_objeto)

                else:
                    print("Opção inválida!")

            elif escolha == '6':
                # Exibir itens cadastrados
                self.exibirItens()
                continue

            elif escolha == '7':
                # Exibir funcionários cadastrados
                self.exibirFuncionarios()
                continue

            elif escolha == '8':
                print("Saindo do sistema de gerenciamento...")
                break

            else:
                print("Opção inválida. Tente novamente.")
    
    def cadastrarItem(self, item):
        self.banco_de_dados.itens[item.codigo] = item
        self.banco_de_dados.contagem_itens['itens'] += 1

    def cadastrarFuncionario(self, funcionario):
        self.banco_de_dados.funcionarios[funcionario.cpf] = funcionario
        self.banco_de_dados.contagem_itens['funcionarios'] += 1

    def removerItem(self, codigo_item):
        if codigo_item in self.banco_de_dados.itens:
            del self.banco_de_dados.itens[codigo_item]
            self.banco_de_dados.contagem_itens['itens'] -= 1
            print(f"Item {codigo_item} removido com sucesso.")
        else:
            print("Item não encontrado no banco de dados.")

    def removerFuncionario(self, cpf_funcionario):
        if cpf_funcionario in self.banco_de_dados.funcionarios:
            del self.banco_de_dados.funcionarios[cpf_funcionario]
            self.banco_de_dados.contagem_itens['funcionarios'] -= 1
            print(f"Funcionário com CPF {cpf_funcionario} removido com sucesso.")
        else:
            print("Funcionário não encontrado no banco de dados.")

    def editarObjeto(self, identificador, tipo_objeto):
        if tipo_objeto == "item":
            objeto = self.banco_de_dados.itens.get(identificador)
        elif tipo_objeto == "funcionario":
            objeto = self.banco_de_dados.funcionarios.get(identificador)
        else:
            print("Tipo de objeto inválido.")
            return

        if not objeto:
            print("Objeto não encontrado.")
            return

        print(f"Dados atuais: {objeto.__dict__}")
        atributo = input("Digite o atributo que deseja editar: ")
        if not hasattr(objeto, atributo):
            print("Atributo não encontrado no objeto.")
            return

        novo_valor = input(f"Digite o novo valor para {atributo}: ")
        try:
            tipo_atual = type(getattr(objeto, atributo))
            novo_valor = tipo_atual(novo_valor)
        except ValueError:
            print("Tipo de dado inválido para o atributo.")
            return
    
        setattr(objeto, atributo, novo_valor)
        print("Objeto editado com sucesso!")

    def exibirItens(self):
        if not self.banco_de_dados.itens:
            print("Nenhum item cadastrado.")
        print(f"Número de itens diferentes: {self.banco_de_dados.contagem_itens['itens']}")
        for codigo, item in self.banco_de_dados.itens.items():
            print(item)

    def exibirFuncionarios(self):
        if not self.banco_de_dados.funcionarios:
            print("Nenhum funcionário cadastrado.")
        print(f"Número de funcionarios: {self.banco_de_dados.contagem_itens['funcionarios']}")
        for cpf, funcionario in self.banco_de_dados.funcionarios.items():
            print(funcionario)