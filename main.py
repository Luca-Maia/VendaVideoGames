import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

# Removendo anos incompletos (2016 em diante)

df = df[df["Year"] < 2016]

# Verificando o intervalo de tempo do dataset
print(f'O dataset cobre de {df["Year"].min()} até {df["Year"].max()}.')


# ---------- Aqui terminanos a limpeza dos dados ----------------


# Vamos começar a análise pelas tendências de mercado

# Identificar os gêneros mais vendidos ao longo dos anos

# Agrupando por Ano e Gênero e somando as vendas globais
vendas_ano_genero = df.groupby(["Year", "Genre"])["Global_Sales"].sum().reset_index()

# Encontrando o gênero com maior volume de vendas para cada ano
idx_max_genero = vendas_ano_genero.groupby(["Year"])["Global_Sales"].idxmax()

generos_campeoes = vendas_ano_genero.loc[idx_max_genero]

print("\nGênero mais vendido em cada ano (últimos 10 anos do dataset):\n")
print(generos_campeoes.tail(10))

# Plotando um gráfico com essas informações

# Configurando o estilo
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 7))

# Criando o gráfico de barras
# Usaremos o DataFrame 'generos_campeoes' que foi filtrado
ax = sns.barplot(
    data=generos_campeoes.tail(10), x="Year", y="Global_Sales", hue="Genre", dodge=False
)

# Títulos e rótulos
plt.title("Gênero Mais Vendido por Ano (Últimos 10 anos)", fontsize=16)
plt.xlabel("Ano", fontsize=12)
plt.ylabel("Vendas Globais (em milhões)", fontsize=12)
plt.legend(title="Gênero", bbox_to_anchor=(1.05, 1), loc="upper left")

plt.tight_layout()
# plt.show()

# Analisar o impacto das editoras no desempenho das vendas
print("\n--- Impacto das Editoras nas Vendas Globais ---\n")
vendas_por_editora = df.groupby("Publisher")["Global_Sales"].sum().reset_index()
top_10_editoras = vendas_por_editora.sort_values(
    by="Global_Sales", ascending=False
).head(10)

# Plotando um gráfico com essas informações

# Configurando o estilo
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 7))

# Criando o gráfico de barras
ax1 = sns.barplot(
    data=top_10_editoras, 
    x="Global_Sales", 
    y="Publisher",
    palette='viridis'
)

# Rótulos de dados
for container in ax.containers:
    ax.bar_label(container, fmt='%.1f', padding=5, fontsize=11, fontweight='bold')

# Títulos e rótulos
plt.title('Top 10 Editoras por Vendas Globais (Mídia Física)', fontsize=14)
plt.xlabel('Vendas acumuladas em Milhões', fontsize=12)
plt.ylabel('')

sns.despine(left=True, bottom=True)

plt.tight_layout() # Ajusta o layout para não cortar os nomes das editoras na esquerda
plt.show()

# Acompanhar as tendências de vendas em todas as regiões

# ANÁLISE COMPARATIVA

# Comparar o desempenho de vendas de diferentes plataformas de jogos (Playstation, Xbox, Wii)

# Avaliar o desempenho de diferentes editoras de jogos em vários mercados
