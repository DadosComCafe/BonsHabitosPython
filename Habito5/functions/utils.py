def valida_tipagem(string: str|int|float) -> bool| str:
    """Verifica se o valor informado é do tipo string

    Args:
        string (str | int | float): Valo que o usuário fornece para passar na validação

    Returns:
        bool| str: True se for string, e uma mensagem informando que não é string, caso não seja.
    """
    if not isinstance(string, str):
        return "Valor fornecido não é do tipo string!"
    return True