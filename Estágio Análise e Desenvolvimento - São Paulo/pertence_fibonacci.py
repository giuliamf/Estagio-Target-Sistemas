"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores
anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado
pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado com qualquer entrada de sua preferência ou pode ser previamente definido no
código;

https://www.linkedin.com/in/giuliamf/
"""


def pertence_fibonacci(numero):
    a, b = 0, 1

    if b == numero or a == numero:
        return f'O número {numero} pertence à sequência de Fibonacci.'

    while b < numero:
        a, b = b, a + b

    if b == numero:
        return f'O número {numero} pertence à sequência de Fibonacci.'
    else:
        return f'O número {numero} não pertence à sequência de Fibonacci.'


n = int(input("Digite um número para descobrir se ele pertence à sequência de Fibonacci: "))
print(pertence_fibonacci(n))
