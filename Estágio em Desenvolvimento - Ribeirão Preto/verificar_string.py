"""2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula,
além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada com qualquer entrada de sua preferência ou pode ser previamente definida
no código;

https://www.linkedin.com/in/giuliamf/
"""
string = input('Digite uma palavra: ')

print(f'A letra "a" aparece {string.lower().count("a")} vezes na palavra "{string}"')
