# graficos_games.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def carregar_dados():
    # Carrega o dataset CSV
    url = 'https://zenodo.org/record/5898311/files/vgsales.csv'
    return pd.read_csv(url)

def grafico_vendas_por_ano(df):
    # Agrupa as vendas globais por ano
    vendas_ano = df.groupby('Year')['Global_Sales'].sum().reset_index()
    vendas_ano = vendas_ano[vendas_ano['Year'].notna()]

    # Plota o gráfico
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Year', y='Global_Sales', data=vendas_ano, marker='o', color='b')
    plt.title('Vendas Globais de Videogames por Ano')
    plt.xlabel('Ano')
    plt.ylabel('Vendas Globais (milhões)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def grafico_vendas_por_genero(df):
    # Agrupa as vendas globais por gênero
    vendas_genero = df.groupby('Genre')['Global_Sales'].sum().reset_index()
    vendas_genero = vendas_genero[vendas_genero['Global_Sales'] > 0]

    # Plota o gráfico
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Global_Sales', y='Genre', data=vendas_genero, palette='viridis')
    plt.title('Vendas Globais por Gênero de Jogo')
    plt.xlabel('Vendas Globais (milhões)')
    plt.ylabel('Gênero')
    plt.tight_layout()
    plt.show()

def grafico_vendas_por_plataforma(df):
    # Agrupa as vendas globais por plataforma
    vendas_plataforma = df.groupby('Platform')['Global_Sales'].sum().reset_index()
    vendas_plataforma = vendas_plataforma[vendas_plataforma['Global_Sales'] > 0]

    # Plota o gráfico
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Global_Sales', y='Platform', data=vendas_plataforma, palette='magma')
    plt.title('Vendas Globais por Plataforma')
    plt.xlabel('Vendas Globais (milhões)')
    plt.ylabel('Plataforma')
    plt.tight_layout()
    plt.show()

def main():
    # Carrega os dados
    df = carregar_dados()

    # Chama as funções para gerar os gráficos
    grafico_vendas_por_ano(df)
    grafico_vendas_por_genero(df)
    grafico_vendas_por_plataforma(df)

if __name__ == "__main__":
    main()
