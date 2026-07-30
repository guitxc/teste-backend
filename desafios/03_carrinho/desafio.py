def calcular_total_carrinho(carrinho: list[dict]) -> float:

    total = 0.0

    for item in carrinho:
        subtotal = item["preco"] * item["quantidade"]

        total += subtotal

    return total

# --- TESTE MANUAL ---
# Pode apagar essa parte depois de ver o resultado!
