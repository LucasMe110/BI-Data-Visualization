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

# Calculando o Ticket Médio Mensal
average_ticket_monthly = sales.groupby('AnoMes')['Amount'].mean()

# Convertendo para um DataFrame para facilitar leitura
average_ticket_df = average_ticket_monthly.reset_index()
average_ticket_df['AnoMes'] = average_ticket_df['AnoMes'].dt.strftime('%Y-%m')

# Criando a pasta charts, se não existir
os.makedirs('charts', exist_ok=True)

# Aplicando o estilo Cyberpunk
plt.style.use("cyberpunk")

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(average_ticket_df['AnoMes'], average_ticket_df['Amount'], marker='o', linestyle='-', color='cyan', label='Average Ticket')
plt.title('Average Ticket Monthly', fontsize=16, color='white')
plt.xlabel('Year and Month', fontsize=12, color='white')
plt.ylabel('Average Ticket (USD)', fontsize=12, color='white')
plt.xticks(rotation=45, color='white')
plt.yticks(color='white')
plt.legend(fontsize=10)

# Adicionando efeitos Cyberpunk
mplcyberpunk.add_glow_effects()

# Salvando o gráfico na pasta charts
output_path = 'charts/Average_Ticket_Monthly.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')

# Fechando o gráfico para liberar memória
plt.close()
