def exporta_txt_com_valor_par(numero: float|int|str) -> str|None:
    """Dado um valor informado, verifica se é par, retornando
    uma mensagem e exportando o valor informado em um txt.

    Args:
        numero (float|int|str): Valor numérico que o usuário deve fornecer.

    Returns:
        str|None: A situação do valor informado se não for inteiro e par, e None caso o contrário.
    """
    if isinstance(numero, str):
        return "Valor do tipo texto, não um valor numérico!"
    
    if isinstance(numero, float):
        return "Valor não inteiro!"
    
    if numero % 2 == 0:
        with open("situacao.txt", "w", encoding="utf-8") as texto:
            texto.write("**************\n")
            texto.write(f"O número informado: {numero} é um número par!")


def confere_tipagem_integer(numero: int|float|str) -> bool:
    """Verifica se o valor informado é do tipo inteiro.

    Args:
        numero (int|float|str): Valor numérico inteiro informado pelo usuário.

    Returns:
        bool: True se for do tipo integer, e False caso contrário.
    """
    return isinstance(numero, int)


def confere_valor_par(numero: int) -> bool:
    """Verifica se o valor 

    Args:
        numero (int): Valor numérico inteiro informado pelo usuário.

    Returns:
        bool: True se for par, False caso contrário. 
    """
    return numero % 2 == 0


def exporta_valor_par(numero: int) -> None:
    """Exporta o valor informado que deve ser par

    Args:
        numero (int): Um número par informado.
    """
    with open("situacao.txt", "w", encoding="utf-8") as texto:
        texto.write("**************\n")
        texto.write(f"O número informado: {numero} é um número par!")