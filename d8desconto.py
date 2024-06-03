valor = float(input('Digite o preço de um produto.'))
desconto = (5 / 100) * valor
total = valor - desconto

print(f'Na liquidação, esse produto terá 5% de desconto, portanto ficará com o preço de {total}R$')