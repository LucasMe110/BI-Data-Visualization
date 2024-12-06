import pandas as pd
import os

# Criação do diretório para os dados limpos, se não existir
os.makedirs('clean_data', exist_ok=True)

# Arquivos de entrada
sales_file = 'data/Sales.csv'
employees_file = 'data/Employees.csv'
customers_file = 'data/Customers.csv'

# Arquivos de saída
clean_sales_file = 'clean_data/Clean_Sales.csv'
clean_employees_file = 'clean_data/Clean_Employees.csv'
clean_customers_file = 'clean_data/Clean_Customers.csv'

# Tratamento de Sales.csv
sales = pd.read_csv(sales_file)

# Conversão de SaleDate para datetime
sales['SaleDate'] = pd.to_datetime(sales['SaleDate'], errors='coerce')

# Removendo linhas com valores ausentes ou inválidos
sales = sales.dropna(subset=['CustomerID', 'EmployeeID', 'SaleDate', 'Amount'])

# Filtrando valores inconsistentes (Ex: Amount negativo ou nulo)
sales = sales[sales['Amount'] > 0]

# Salvando o arquivo limpo
sales.to_csv(clean_sales_file, index=False)
print(f"Arquivo limpo salvo: {clean_sales_file}")

# Tratamento de Employees.csv
employees = pd.read_csv(employees_file)

# Verificando tipos de dados
employees['TasksCompleted'] = pd.to_numeric(employees['TasksCompleted'], errors='coerce')
employees['SalesGenerated'] = pd.to_numeric(employees['SalesGenerated'], errors='coerce')
employees['PerformanceScore'] = pd.to_numeric(employees['PerformanceScore'], errors='coerce')

# Removendo linhas com informações ausentes
employees = employees.dropna()

# Salvando o arquivo limpo
employees.to_csv(clean_employees_file, index=False)
print(f"Arquivo limpo salvo: {clean_employees_file}")

# Tratamento de Customers.csv
customers = pd.read_csv(customers_file)

# Conversão de datas para datetime
customers['SignupDate'] = pd.to_datetime(customers['SignupDate'], errors='coerce')
customers['LastPurchaseDate'] = pd.to_datetime(customers['LastPurchaseDate'], errors='coerce')

# Filtrando status válidos
valid_statuses = ['Ativo', 'Inativo', 'Pendente']
customers = customers[customers['Status'].isin(valid_statuses)]

# Removendo linhas com informações ausentes
customers = customers.dropna(subset=['CustomerID', 'Name', 'SignupDate'])

# Salvando o arquivo limpo
customers.to_csv(clean_customers_file, index=False)
print(f"Arquivo limpo salvo: {clean_customers_file}")
