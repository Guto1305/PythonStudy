largura = float(input('Quanto sua parede mede de largura?: '))
altura = float(input('Quanto sua parede mede de altura?: '))
area = altura * largura
tinta = 2
total = area * tinta

print(f'Sua parede tem uma área de {area} metros²')
print(f'Considerando que uma lata de tinta pinte 2m² da sua parede, você irá precisar de {total} latas de tinta.')