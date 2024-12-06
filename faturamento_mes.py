import pandas as pd
import matplotlib.pyplot as plt
import mplcyberpunk  # Tema Cyberpunk
import os

# Carregando os dados tratados
sales_file = 'clean_data/Clean_Sales.csv'
sales = pd.read_csv(sales_file)

# Garantindo que a coluna SaleDate esteja no formato datetime
sales['SaleDate'] = pd.to_datetime(sales['SaleDate'])

# Extraindo o ano e o mês para agrupar os dados
sales['AnoMes'] = sales['SaleDate'].dt.to_period('M')

# Calculando o Faturamento Mensal
revenue_monthly = sales.groupby('AnoMes')['Amount'].sum()

# Convertendo para DataFrame para facilitar leitura
revenue_df = revenue_monthly.reset_index()

# Formatando o AnoMes para string para exibição no gráfico
revenue_df['AnoMes'] = revenue_df['AnoMes'].dt.strftime('%Y-%m')

# Criando a pasta charts, se não existir
os.makedirs('charts', exist_ok=True)

# Aplicando o estilo Cyberpunk
plt.style.use("cyberpunk")

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(revenue_df['AnoMes'], revenue_df['Amount'], marker='s', linestyle='-', color='#9b59b6', label='Monthly Revenue')  # Roxo mais claro

# Personalização do gráfico
plt.title('Monthly Revenue', fontsize=16, color='white')
plt.xlabel('Year and Month', fontsize=12, color='white')
plt.ylabel('Revenue (USD)', fontsize=12, color='white')
plt.xticks(rotation=45, color='white')
plt.yticks(color='white')
plt.legend(fontsize=10)

# Adicionando efeitos Cyberpunk
mplcyberpunk.add_glow_effects()

# Salvando o gráfico na pasta charts
output_path = 'charts/Monthly_Revenue.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')

# Fechando o gráfico para liberar memória
plt.close()

print(f"Gráfico salvo em: {output_path}")
