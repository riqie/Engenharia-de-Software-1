from bancoDados import BancoDeDados
from veiculo import Veiculo
from servico import Servico
from cliente import Cliente
from datetime import date
from typing import Type
from orcamento import Orcamento
from datetime import datetime
from produto import Produto
from maoObra import MaoObra
from validarentrada import *

class ControladorOrcamento:
    def __init__(self, banco_de_dados: BancoDeDados):
        self.banco_de_dados = banco_de_dados

    def menuOrcamento(self):
        while True:
            print("\n===== Menu de Orçamentos =====")
            print("1. Criar um novo orçamento")
            print("2. Editar um orçamento existente")
            print("3. Excluir um orçamento")
            print("4. Listar todos os orçamentos")
            print("5. Voltar")
            
            escolha = input("Escolha uma opção: ")
            
            if escolha == '1':
                print("---- Dados do veículo ----")
                codigo = input("Digite o código do orçamento: ")
                data_objeto = validar_data("Digite a data de entrada (dd/mm/aaaa): ")
                veiculo_nome = input("Digite o nome do veículo: ")
                veiculo_quilometragem = validar_int("Digite a quilometragem do veículo: ")
                veiculo_montadora = input("Digite a montadora do veículo: ")
                veiculo_placa = input("Digite a placa do veículo: ")
                veiculo_ano = validar_int("Digite o ano do veículo: ")
                veiculo_chassi = input("Digite o chassi do veículo: ")
                veiculo_frota = input("Digite a frota do veículo: ")
                
                print("---- Dados do cliente ----")
                cliente_nome = input("Digite o nome do cliente: ")
                cliente_telefone = input("Digite o telefone do cliente: ")
                cliente_seguradora = input("Digite a seguradora do cliente: ")

                print("---- Dados do serviço ----")
                tipo_produto = input("Digite o tipo do produto que sera utlizado no serviço: ")
                valor_produto = validar_float("Digite o valor do produto: ")
                quantidade_produto = validar_int("Digite a quantidade do produto: ")

                descricao_maoObra = input("Digite a descrição da mao de obra: ")
                preco_maoObra = validar_float("Digite o preço da mao de obra: ")

                produto = Produto(tipo_produto, valor_produto, quantidade_produto)
                maoObra = MaoObra(descricao_maoObra, preco_maoObra)
                veiculo = Veiculo(veiculo_nome, veiculo_quilometragem, veiculo_montadora, veiculo_placa, veiculo_ano, veiculo_chassi, veiculo_frota)
                servico = Servico(produto, maoObra)
                cliente = Cliente(cliente_nome, cliente_telefone, cliente_seguradora)
                
                self.novoOrcamento(codigo, data_objeto, veiculo, servico, cliente)
            
            elif escolha == '2':
                if self.banco_de_dados.contagem_itens['orcamentos'] == 0:
                    print("Não existem orçamentos ainda.")
                    continue
                codigo = input("Digite o código do orçamento a ser editado: ")
                orcamento_obj = self.banco_de_dados.orcamentos.get(codigo) 
                if not orcamento_obj:
                    print(f"Orçamento com código {codigo} não encontrado.")
                    continue
                
                print("Deixe em branco para não alterar um campo.")
                nova_data_entrada_str = input("Digite a nova data de entrada (aaaa-mm-dd, deixe em branco para manter): ")
                nova_data_entrada = date.fromisoformat(nova_data_entrada_str) if nova_data_entrada_str else None
                
                novo_veiculo_nome = input("Digite o novo nome do veículo (deixe em branco para não alterar): ")
                novo_veiculo_quilometragem_str = input("Digite a nova quilometragem do veículo (deixe em branco para não alterar): ")
                novo_veiculo_quilometragem = float(novo_veiculo_quilometragem_str) if novo_veiculo_quilometragem_str else None

                novo_cliente_nome = input("Digite o novo nome do cliente (deixe em branco para não alterar): ")
                novo_cliente_telefone = input("Digite o novo telefone do cliente (deixe em branco para não alterar): ")

                self.editarOrcamento(codigo, nova_data_entrada, novo_veiculo_nome, novo_veiculo_quilometragem, None, novo_cliente_nome, novo_cliente_telefone)

            elif escolha == '3':
                if self.banco_de_dados.contagem_itens['orcamentos'] == 0:
                    print("Não existem orçamentos ainda.")
                    continue
                codigo = input("Digite o código do orçamento a ser excluído: ")
                self.excluirOrcamento(codigo)
            
            elif escolha == '4':
                self.listarOrcamentos()
            
            elif escolha == '5':
                print("Saindo do sistema...")
                break
            
            else:
                print("Opção inválida. Tente novamente.\n")

        

    def novoOrcamento(self, codigo: str, data_entrada: date, veiculo: Veiculo, servico: Servico, cliente: Cliente):

        orcamento = Orcamento(codigo, data_entrada, veiculo, servico, cliente)
        self.banco_de_dados.orcamentos[codigo] = orcamento
        self.banco_de_dados.contagem_itens['orcamentos'] += 1
        print(f"Orçamento {codigo} criado com sucesso!")

    def editarOrcamento(self, codigo: str, nova_data_entrada: datetime.date = None, novo_veiculo_nome: str = None, 
                        novo_veiculo_quilometragem: float = None, nova_descricao_servico: str = None, 
                        novo_cliente_nome: str = None, novo_cliente_telefone: str = None):
        
        orcamento = self.banco_de_dados.orcamentos.get(codigo)
        if orcamento:
            if nova_data_entrada:
                orcamento.definir_Data(nova_data_entrada)
            if novo_veiculo_nome:
                orcamento.obter_Veiculo().definir_Nome(novo_veiculo_nome)
            if novo_veiculo_quilometragem is not None:
                orcamento.obter_Veiculo().definir_Quilometragem(novo_veiculo_quilometragem)
            if novo_cliente_nome:
                orcamento.obter_Cliente().definir_Nome(novo_cliente_nome)  
            if novo_cliente_telefone:
                orcamento.obter_Cliente().definir_Telefone(novo_cliente_telefone)

            print(f"Orçamento {codigo} atualizado com sucesso!")
        else:
            print(f"Orçamento com código {codigo} não encontrado.")

    def excluirOrcamento(self, codigo: str):
        
        if codigo in self.banco_de_dados.orcamentos:
            del self.banco_de_dados.orcamentos[codigo]
            self.banco_de_dados.contagem_itens['orcamentos'] -= 1
            print(f"Orçamento {codigo} excluído com sucesso!")
        else:
            print(f"Orçamento com código {codigo} não encontrado.")

    def listarOrcamentos(self):
        if not self.banco_de_dados.orcamentos:
            print("Não há orçamentos registrados.")
        else:
            print("--------------------------------------------------")
            print(f"Número de orçamentos diferentes: {self.banco_de_dados.contagem_itens['orcamentos']}")
            counter = 1
            for orcamento in self.banco_de_dados.orcamentos.values():
                print(f"{counter})")
                print(orcamento.juntarInfo())
            counter += 1

    def menuInicial(self):
        return 