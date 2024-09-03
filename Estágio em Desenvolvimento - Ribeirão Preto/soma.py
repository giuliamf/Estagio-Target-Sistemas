"""
3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?

https://www.linkedin.com/in/giuliamf/
"""

indice, soma, k = 12, 0, 1

while k < indice:
    k += 1
    soma += k

print(soma)
