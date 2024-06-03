num: float
cent: float
mili: float

num = int(input('Digite um valor em metros: '))
cent = (num * 100)
mili = (num * 1000)

print(f'Esse valor tem {num} metros, {cent} centímetros e {mili} milímetros.')