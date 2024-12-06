import pandas as pd
import matplotlib.pyplot as plt
import mplcyberpunk
import os

# Carregar os dados limpos
clean_employees_file = 'clean_data/Clean_Employees.csv'
employees = pd.read_csv(clean_employees_file)

# Garantir que a pasta charts exista
os.makedirs('charts', exist_ok=True)

# Ordenar os funcionários pelo desempenho (SalesGenerated)
employees = employees.sort_values(by='SalesGenerated', ascending=False)

# Criar o gráfico de barras
plt.figure(figsize=(14, 8))
plt.bar(employees['Name'], employees['SalesGenerated'], color='cyan', edgecolor='white')

# Aplicar o tema Cyberpunk
plt.style.use("cyberpunk")
mplcyberpunk.add_glow_effects()

# Adicionar títulos e rótulos
plt.title("Desempenho dos Funcionários - Vendas Geradas", fontsize=18, color='white')
plt.xlabel("Funcionário", fontsize=14, color='white')
plt.ylabel("Vendas Geradas", fontsize=14, color='white')
plt.xticks(rotation=45, ha='right', color='white')
plt.yticks(color='white')

# Ajustar o layout para melhorar a visualização
plt.tight_layout()

# Salvar o gráfico na pasta charts
chart_path = 'charts/employee_performance.png'
plt.savefig(chart_path, dpi=300, transparent=False)
