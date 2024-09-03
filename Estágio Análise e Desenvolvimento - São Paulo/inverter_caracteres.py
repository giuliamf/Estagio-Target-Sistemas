"""
5) Escreva um programa que inverta os caracteres de uma string.

IMPORTANTE:
a) Essa string pode ser informada com qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;

https://www.linkedin.com/in/giuliamf/
"""

string1 = input("Digite uma string para inverter seus caracteres com a primeira opção: ")
print(string1[::-1])

# Outra função:


def inverter_caracteres(string):
    string_invertida = ''
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida


string2 = input("Digite uma string para inverter seus caracteres com a segunda opção: ")
print(inverter_caracteres(string2))

