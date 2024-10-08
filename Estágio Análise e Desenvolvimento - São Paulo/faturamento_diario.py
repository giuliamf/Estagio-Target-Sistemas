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

with open('dados.json') as arquivo:
    faturamento = json.load(arquivo)

faturamento_diario = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

dias_acima_da_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

print(f"Menor valor de faturamento: {menor_valor:.2f}")
print(f"Maior valor de faturamento: {maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
