from datetime import date

def validar_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("Valor inválido, tente novamente.")
                continue
            return valor
        except ValueError:
            print("Valor inválido, tente novamente.")

def validar_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("Valor inválido, tente novamente.")
                continue
            return valor
        except ValueError:
            print("Valor inválido, tente novamente.")

def validar_data(mensagem):
    while True:
        try:
            valor = input(mensagem)
            dia, mes, ano = map(int, valor.split('/'))
            return date(ano, mes, dia)
        except (ValueError, TypeError):
            print("Data inválida. Certifique-se de usar o formato DD/MM/AAAA e tente novamente.")