def senha_forte(senha: str) -> bool:

    # Padrão de Mercado com REGEX

    padrao = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{9,}$"

    if re.match(padrao, senha):
        return True
    
    return False

    # Jeito simples
    
    # return (
    # len(senha) > 8 and
    # any(letra.isupper() for letra in senha) and
    # any(letra.islower() for letra in senha) and
    # any(letra.isdigit() for letra in senha)
    # )
