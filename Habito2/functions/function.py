def soma_de_inteiros(x: int, y: int) -> int:
    """Realiza a some de dois números inteiros informados pelo usuário

    Args:
        x (int): O primeiro valor inteiro
        y (int): O segundo valor inteiro

    Returns:
        int:O resultado da soma, de x e y.
    """
    z = x + y
    return z



if __name__ == "__main__":
    print(f" A soma de 5 e 6 é: {soma_de_inteiros(5,6)}")