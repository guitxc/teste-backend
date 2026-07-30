import re

def email_valido(email: str) -> bool:
    # Padrão de Mercado com REGEX
    molde = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    
    if re.match(molde, email):
        return True
    else:
        return False

    # Jeito mais simples
    
    # if "@" in email and "." in email:
    #     return True
    # return False