import re

def senha_forte(senha: str) -> bool:
    padrao = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
    return bool(re.match(padrao, senha))

    # Jeito simples

    # return (
    # len(senha) > 8 and
    # any(letra.isupper() for letra in senha) and
    # any(letra.islower() for letra in senha) and
    # any(letra.isdigit() for letra in senha)
    # )
