"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do
valor total mensal da distribuidora.  

https://www.linkedin.com/in/giuliamf/
"""
faturamento_mensal = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_faturamento = sum(faturamento_mensal.values())
percentuais = {estado: (faturamento / total_faturamento) * 100 for estado, faturamento in faturamento_mensal.items()}
print("Percentual de representação de cada estado no faturamento mensal da distribuidora:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
