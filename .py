import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset
df = pd.read_csv('vgsales.csv')

# Contar o número de jogos por gênero
genre_counts = df['Genre'].value_counts()

# Criar o gráfico
plt.figure(figsize=(10, 6))
genre_counts.plot(kind='bar', color='skyblue')
plt.title('Número de Jogos por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Quantidade de Jogos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
