def calcula_percentual_estados(faturamento_estados):
  """Calcula o percentual de representação de cada estado no faturamento total.

  Args:
    faturamento_estados: Um dicionário onde as chaves são os estados e os valores são os faturamentos.

  Returns:
    Um dicionário com os estados como chaves e os percentuais como valores.
  """

  # Calcula o faturamento total
  faturamento_total = sum(faturamento_estados.values())

  # Calcula o percentual de cada estado
  percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_estados.items()}

  return percentuais

# Dados de entrada (substitua pelos seus dados)
faturamento = {
  "SP": 67836.43,
  "RJ": 36678.66,
  "MG": 29229.88,
  "ES": 27165.48,
  "Outros": 19849.53
}

# Chama a função e imprime os resultados
resultados = calcula_percentual_estados(faturamento)
for estado, percentual in resultados.items():
  print(f"{estado}: {percentual:.2f}%")