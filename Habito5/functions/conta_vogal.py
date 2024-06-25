from .utils import valida_tipagem
import re


def conta_vogal(string: str) -> int|str:
    """Conta o número de vogais utilizando expressão regular, de dada string

    Args:
        string (str): String a qual será feita a contagem

    Returns:
        (int|str): Número de vogais ou mensagem de erro.
    """
    verificacao = valida_tipagem(string=string)
    if verificacao != True:
        return verificacao

    pattern = re.compile(r'[aeiouAEIOU]')

    vogais = pattern.findall(string)

    return len(vogais)


if __name__ == "__main__":

    print(f"O múmero de vogais em 'Python' é: {conta_vogal('Python')}")
