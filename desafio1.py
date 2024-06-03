num: int
ant: int
suc: int

num = int(input('Digite um número para calcular seu antecessor e seu sucessor: '))
suc = num + 1
ant = num - 1

print(f'Sucessor = {suc}, Antecessor = {ant}')