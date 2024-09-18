import json

with open('dados.json') as file:
    dados = json.load(file)

faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0] 

menor_valor = min(faturamentos)
maior_valor = max(faturamentos)
media_mensal = sum(faturamentos) / len(faturamentos)
dias_acima_da_media = len([valor for valor in faturamentos if valor > media_mensal])

print(f"O maior valor de faturamento diário foi de: R${maior_valor:.2f}, o menor valor de faturamento diário foi de: R$ {menor_valor:.2f}, e os dias em que o faturamento foi superior à média mensal: {dias_acima_da_media}")