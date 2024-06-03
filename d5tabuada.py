
produto: int
tabuada: int
num = int(input('Digite um número para calcular a tabuada'))

for i in range(1,11):
    produto = num * i
    print(f'{num} x {i} = {produto}')