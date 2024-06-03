num1: float
num2: float
s: float
d: float
m: float
e: float
di: float
sub: float 

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
s = num1 + num2
d = num1 / num2
di = num1 // num2
m = num1 * num2
e = num1 ** num2
sub = num1 - num2
print(f'Soma = {s}, Subtração = {sub}, Divisão = {d}, Multiplicação = {m}, Divisão Inteira = {di}, Potência = {e}')
