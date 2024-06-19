from functions.function import function1
from functions.function import function2

print(f"O nome deste módulo: {__name__}")

print(f"O nome do módulo importado para function1: {function1.__name__}")

print(f"O nome do módulo importado para function2: {function2.__name__}")