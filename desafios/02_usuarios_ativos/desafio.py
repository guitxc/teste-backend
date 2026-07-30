def filtrar_usuarios_ativos(usuarios: list) -> list:
    usuarios_ativos = []
    
    for usuario in usuarios:
        if usuario["ativo"]:
            usuarios_ativos.append(usuario["nome"])
    
    return usuarios_ativos

    # OU return [usuario["nome"] for usuario in usuarios if usuario["ativo"]]