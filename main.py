import pandas as pd

# Este conjunto de dados contém informações sobre vendas de videogames em diferentes
# plataformas, gêneros e regiões, tornando-o valioso para diversas aplicações analíticas e
# comerciais.

df = pd.read_csv("vgsales.csv")

# 1. Inspeção inicial

# Visualizar as 5 primeiras linhas (para entender o formato das colunas)
print(df.head())

# Verificar o tamanho do dataset (linhas, colunas)
print(f"Tamanho do dataset: {df.shape}")

# Ver os tipos de dados de cada coluna (int, float, object/string) e uso de memória
print(df.info())

# 2. Identificar e tratar valores nulos ou duplicados

# Verificar a quantidade de valores nulos (vazios) por coluna
print(df.isnull().sum())

# Verificar se existem linhas exatamente duplicadas
print(f"Linhas duplicadas: {df.duplicated().sum()}")

# Existem 271 linhas da coluna 'Year' nulas e 58 da coluna 'Publisher', iremos removê-las

# Removendo linhas nulas das colunas 'Year' e 'Publisher'
df.dropna(subset=["Year", "Publisher"], inplace=True)

# Verificando se a remoção deu certo e conferindo o novo tamanho do dataset

print("Valores nulos após a limpeza: ")
print(df.isnull().sum())
print(f"Novo tamanho do dataset: {df.shape}")

# Convertendo a coluna 'Year' para int

df["Year"] = df["Year"].astype(int)

print(df[["Name", "Year"]].head())

# Verificando o intervalo de tempo do dataset
print(f'O dataset cobre de {df["Year"].min()} até {df["Year"].max()}.')

# Aqui terminanos a limpeza dos dados ----------------------------------------

# Vamos começar a análise pelas tendências de mercado

# Identificar os gêneros e plataformas mais vendidos ao longo dos anos

# Agrupando por Ano e Gênero e somando as vendas globais
vendas_ano_genero = df.groupby(["Year", "Genre"])["Global_Sales"].sum().reset_index()

# Encontrando o gênero com maior volume de vendas para cada ano
idx_max_genero = vendas_ano_genero.groupby(["Year"])["Global_Sales"].idxmax()

generos_campeoes = vendas_ano_genero.loc[idx_max_genero]

print('Gênero mais vendido em cada ano (últimos 10 anos do dataset):')
print(generos_campeoes.tail(10))



# Analisar o impacto das editoras no desempenho das vendas

# Acompanhar as tendências de vendas em todas as regiões

# ANÁLISE COMPARATIVA

# Comparar o desempenho de vendas de diferentes plataformas de jogos (Playstation, Xbox, Wii)

# Avaliar o desempenho de diferentes editoras de jogos em vários mercados
