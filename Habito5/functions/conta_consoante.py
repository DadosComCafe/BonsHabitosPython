from .utils import valida_tipagem
import re


def conta_consoante(string: str) -> int|str:
    """Conta o número de consoantes utilizando expressão regular, de dada string

    Args:
        string (str): String a qual será feita a contagem

    Returns:
        (int|str): Número de consoantes ou mensagem de erro.
    """
    verificacao = valida_tipagem(string=string)
    if verificacao != True:
        return verificacao

    pattern = re.compile(r'[^aeiouAEIOU\s\d\W]')

    consoantes = pattern.findall(string)

    return len(consoantes)


if __name__ == "__main__":

    print(f"O múmero de consoantes em 'Python' é: {conta_consoante('Python')}")