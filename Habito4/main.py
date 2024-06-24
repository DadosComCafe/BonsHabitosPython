from functions import confere_tipagem_integer, confere_valor_par, exporta_valor_par

valor = 26

if confere_tipagem_integer(numero=valor) and confere_valor_par(numero=valor):
    exporta_valor_par(numero=valor)
    print("Txt criado com sucesso!")
else:
    print(f"Valor informado: {valor}, não é do tipo inteiro e/ou par!")