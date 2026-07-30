import re

def limpar_csv_numeros(linha: str) -> str:
    return re.sub(r'(?<=\d),(?=\d)', '.', linha)

    # Jeito simples

    # return linha.replace(",", ".")