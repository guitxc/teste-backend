def padronizar_nomes(nomes: list[str]) -> list[str]:

    nomes_padronizados = []

    for nome in nomes:

        nome_limpo = nome.strip().title()

        nomes_padronizados.append(nome_limpo)

    return nomes_padronizados
    # OU return [nome.strip().title() for nome in nomes]