"""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que
desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo
da média;

https://www.linkedin.com/in/giuliamf/
"""
import json

with open("dados.json", "r") as file:
    faturamento_mensal = json.load(file)

faturamento_diario = list(faturamento_mensal.values())
menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)
media_mensal = sum(faturamento_diario) / len(faturamento_diario)
dias_acima_media = len([faturamento for faturamento in faturamento_diario if faturamento > media_mensal])

print(f"O menor valor de faturamento ocorrido em um dia do mês foi de R${menor_faturamento:.2f}")
print(f"O maior valor de faturamento ocorrido em um dia do mês foi de R${maior_faturamento:.2f}")
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {dias_acima_media}")
