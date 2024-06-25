from functions import conta_vogal, conta_consoante


if __name__ == "__main__":
    
    string = "Python is the most powerfull language to learn"

    numero_vogal = {palavra: conta_vogal(palavra) for palavra in string.split(" ")}

    lista_vogal = [conta_vogal(palavra) for palavra in string.split(" ")]

    numero_consoante = {palavra: conta_consoante(palavra) for palavra in string.split(" ")}

    lista_consoante = [conta_consoante(palavra) for palavra in string.split(" ")]

    print(f"A string: {string}")
    print(f"Lista Vogal: {lista_vogal}")
    print(f"Lista Consoante: {lista_consoante}")
    print(f"Dicionário do número de vogais: {numero_vogal}")
    print(f"Dicionário do número de consoantes: {numero_consoante}")