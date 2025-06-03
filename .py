import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('vgsales.csv')

# Contar o número de jogos por gênero
genre_counts = df['Genre'].value_counts()

# Gráfico 1 - Distribuição de Vendas por Gênero
plt.figure(figsize=(10, 6))
genre_counts.plot(kind='bar', color='skyblue')
plt.title('Número de Jogos por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Quantidade de Jogos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Agrupar por plataforma e somar as vendas globais
platform_sales = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False)

# Gráfico 2 - Vendas Globais por Plataforma
plt.figure(figsize=(10, 6))
platform_sales.plot(kind='bar', color='lightgreen')
plt.title('Vendas Globais por Plataforma')
plt.xlabel('Plataforma')
plt.ylabel('Vendas Globais (milhões)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Contar o número de lançamentos por ano
yearly_releases = df['Year'].value_counts().sort_index()

# Gráfico 3 - Tendência de Lançamentos ao Longo dos Anos
plt.figure(figsize=(10, 6))
yearly_releases.plot(kind='line', marker='o', color='coral')
plt.title('Número de Lançamentos de Jogos por Ano')
plt.xlabel('Ano')
plt.ylabel('Número de Lançamentos')
plt.tight_layout()
plt.show()
