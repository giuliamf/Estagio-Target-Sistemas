"""
4) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___
b) 2, 4, 8, 16, 32, 64, ____
c) 0, 1, 4, 9, 16, 25, 36, ____
d) 4, 16, 36, 64, ____
e) 1, 1, 2, 3, 5, 8, ____
f) 2,10, 12, 16, 17, 18, 19, ____

https://www.linkedin.com/in/giuliamf/
"""
a = [1, 3, 5, 7]
b = [2, 4, 8, 16, 32, 64]
c = [0, 1, 4, 9, 16, 25, 36]
d = [4, 16, 36, 64]
e = [1, 1, 2, 3, 5, 8]
f = [2, 10, 12, 16, 17, 18, 19]

print(f'a) Aumenta de 2 em 2: {"".join(str(i) + ", " for i in a)}{a[-1] + 2}')
print(f'b) Multiplica cada um por 2: {"".join(str(i) + ", " for i in b)}{b[-1] * 2}')
print(f'c) Quadrados perfeitos: {"".join(str(i) + ", " for i in c)}{len(c) ** 2}')
print(f'd) Quadrados perfeitos dos números pares: {"".join(str(i) + ", " for i in d)}{((len(d) * 2) + 2) ** 2}')
print(f'e) Fibonacci: {"".join(str(i) + ", " for i in e)}{e[-1] + e[-2]}')
print(f'f) Números que começam com a letra "D": {"".join(str(i) + ", " for i in f)}{200}')
