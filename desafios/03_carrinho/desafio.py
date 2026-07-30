def calcular_total_carrinho(carrinho: list[dict]) -> float:

    total = 0.0

    for item in carrinho:
        subtotal = item["preco"] * item["quantidade"]

        total += subtotal

    return total
    # OU return sum(item["preco"] * item["quantidade"] for item in carrinho)