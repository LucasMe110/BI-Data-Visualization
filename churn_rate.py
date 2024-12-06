import pandas as pd
import matplotlib.pyplot as plt
import os

# Carregando os dados tratados
customers_file = 'clean_data/Clean_Customers.csv'
customers = pd.read_csv(customers_file)

# Garantindo que as colunas de data estejam no formato datetime
customers['SignupDate'] = pd.to_datetime(customers['SignupDate'])
customers['LastPurchaseDate'] = pd.to_datetime(customers['LastPurchaseDate'])

# Extraindo o ano e o mês do LastPurchaseDate
customers['AnoMes'] = customers['LastPurchaseDate'].dt.to_period('M')

# Filtrando clientes inativos
clientes_inativos = customers[customers['Status'] == 'Inativo']

# Contando o total de clientes e inativos por mês
total_clientes_por_mes = customers.groupby('AnoMes').size()
clientes_inativos_por_mes = clientes_inativos.groupby('AnoMes').size()

# Calculando o Churn Rate (evitando divisão por zero)
churn_rate = (clientes_inativos_por_mes / total_clientes_por_mes).fillna(0) * 100

# Convertendo para DataFrame para visualização
churn_rate_df = churn_rate.reset_index()
churn_rate_df.columns = ['AnoMes', 'ChurnRate']

# Criando a pasta charts, se não existir
os.makedirs('charts', exist_ok=True)

# Criando o gráfico com fundo branco
plt.figure(figsize=(10, 6), facecolor='white')  # Define o fundo como branco
plt.plot(churn_rate_df['AnoMes'].astype(str), churn_rate_df['ChurnRate'], marker='o', color='red', label='Churn Rate')
plt.title('Churn Rate Over Time', fontsize=16, color='black')  # Ajustando o texto para cor preta
plt.xlabel('Year and Month', fontsize=12, color='black')
plt.ylabel('Churn Rate (%)', fontsize=12, color='black')
plt.xticks(rotation=45, color='black')  # Ajustando as cores dos ticks
plt.yticks(color='black')
plt.legend(fontsize=10, loc='upper right')

# Salvando o gráfico na pasta charts
output_path = 'charts/Churn_Rate'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')  # Salva com fundo branco

# Fechando o gráfico para liberar memória
plt.close()

# Mensagem informando onde o gráfico foi salvo
print(f"Gráfico salvo em: {output_path}")
