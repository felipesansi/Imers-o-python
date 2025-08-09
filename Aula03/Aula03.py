import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pycountry as pc

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")
#mostrando as primeiras linhas do DataFrame
print(df.head())
print("---------------------------\n")
# moostras as informações do DataFrame
print(df.info())
print("---------------------------\n")
# mostrando as estatísticas descritivas do DataFrame
print(df.describe())
# mostrando o tamanho do DataFrame
print("---------------------------\n")
print(df.shape)

linhas = df.shape[0]
colunas = df.shape[1]

print(f"Linhas: {linhas}, Colunas: {colunas}")
print("---------------------------\n")
print(df.columns)
print("---------------------------\n")

# Dicionário de tradução das colunas
traducao_colunas = {
    'work_year': 'ano',
    'experience_level': 'experiencia',
    'employment_type': 'tipo_emprego',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda_salario',
    'salary_in_usd': 'salario_usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'local_empresa',
    'company_size': 'porte_empresa'
}

# Traduzindo as colunas
df = df.rename(columns=traducao_colunas)

print("Colunas traduzidas:")
print(df.columns)
print("---------------------------\n")

# contando os valores únicos na coluna 'experiencia'
print(df['experiencia'].value_counts())
print("---------------------------\n")

# contando os valores únicos na coluna 'porte_empresa'
print(df['porte_empresa'].value_counts())
print("---------------------------\n")

# contando os valores únicos na coluna 'tipo_emprego'
print(df['tipo_emprego'].value_counts())
print("---------------------------\n")
print(df['remoto'].value_counts())
print("---------------------------\n")
print(df['local_empresa'].value_counts())
print("---------------------------\n")
print(df['salario'].value_counts())
print("---------------------------\n")
print(df['cargo'].value_counts())
print("---------------------------\n")
print(df['residencia'].value_counts())
print("---------------------------\n")

# Mapas de tradução das siglas para pt-br
mapa_experiencia = {'EX': 'Executivo', 'SE': 'Sênior', 'MI': 'Pleno', 'EN': 'Júnior'}
mapa_tipo_emprego = {'FT': 'Tempo integral', 'PT': 'Meio período', 'CT': 'Contrato', 'FL': 'Freelancer'}
mapa_porte_empresa = {'S': 'Pequena', 'M': 'Média', 'L': 'Grande'}

# Países (exemplo para alguns códigos mais comuns, adicione outros conforme necessário)
mapa_paises = {
    'US': 'Estados Unidos',
    'GB': 'Reino Unido',
    'CA': 'Canadá',
    'DE': 'Alemanha',
    'IN': 'Índia',
    'PT': 'Portugal',
    'BR': 'Brasil',
    'ES': 'Espanha',
    'FR': 'França',
    'NL': 'Holanda',
    'GR': 'Grécia',
    'IT': 'Itália',
    'JP': 'Japão',
    'PL': 'Polônia',
    'RU': 'Rússia',
    'TR': 'Turquia',
    'UA': 'Ucrânia',
    'AE': 'Emirados Árabes Unidos',
    'CH': 'Suíça',
    'AT': 'Áustria',
    'IE': 'Irlanda',
    'AU': 'Austrália',
    'BE': 'Bélgica',
    'DK': 'Dinamarca',
    'FI': 'Finlândia',
    'HU': 'Hungria',
    'LU': 'Luxemburgo',
    'MX': 'México',
    'NG': 'Nigéria',
    'NZ': 'Nova Zelândia',
    'RO': 'Romênia',
    'SG': 'Singapura',
    'SI': 'Eslovênia',
    'ZA': 'África do Sul',

}
mapa_remoto = {0: 'presencial', 50: 'hibrido', 100: 'remoto'}


# Aplicando as traduções
df['experiencia'] = df['experiencia'].replace(mapa_experiencia);
df['tipo_emprego'] = df['tipo_emprego'].replace(mapa_tipo_emprego);
df['porte_empresa'] = df['porte_empresa'].replace(mapa_porte_empresa);
df['residencia'] = df['residencia'].replace(mapa_paises);
df['local_empresa'] = df['local_empresa'].replace(mapa_paises);
df['remoto'] = df['remoto'].replace(mapa_remoto);
print("---------------------------\n")
print(df.head()) # mostrando as primeiras linhas do DataFrame após as traduções
print("---------------------------\n")
print(df.isnull().sum()) # mostrando a quantidade de valores nulos em cada coluna
print("---------------------------\n")
print(df['ano'].unique()) # mostrando os anos únicos no DataFrame
print("---------------------------\n")


# Criando um DataFrame  
df_salarios = pd.DataFrame({'nome': ['Guilherme', 'João', 'Maria', 'Ana','Felipe'],
                            'salario': [1000, np.nan, 3000,np.nan,10000]});

df_salarios["media_salario"] = df_salarios['salario'].fillna(df_salarios['salario'].mean().__round__(2));

print(df_salarios);
print("---------------------------\n");
df_salarios["mediana_salario"] = df_salarios['salario'].fillna(df_salarios['salario'].median());
print(df_salarios);
print("---------------------------\n");

# Criando um DataFrame de clima

df_clima = pd.DataFrame({
    'Dia': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'],
    'Temperatura': [30, 32, np.nan, 25, 28, np.nan, 27]
})
df_clima['temperatura_preenchida'] = df_clima['Temperatura'].ffill() # Preenchendo valores nulos com o valor anterior
print(df_clima)
print("---------------------------\n")
df_clima['temperatura_bpreenchida'] = df_clima['Temperatura'].bfill() # Preenchendo valores nulos com o valor seguinte
print(df_clima)
print("---------------------------\n")
df_cidades = pd.DataFrame({'nome': ['Guilherme', 'João', 'Maria', 'Ana','Felipe'],
                            'cidade': ['São Paulo', 'Rio de Janeiro', np.nan, 'Curitiba', np.nan]
                            });

df_cidades["cidade_preenchida"] = df_cidades['cidade'].fillna("Não informado"); # Preenchendo valores nulos com "Não informado"
print(df_cidades);
print("---------------------------\n");
dflimpo = df.dropna()  # Removendo linhas com valores nulos
print(dflimpo.isnull().sum())  # Verificando se ainda há valores nulos
print("---------------------------\n");
print(dflimpo.head())  # Mostrando as primeiras linhas do DataFrame limpo
print("---------------------------\n")
print(dflimpo.info())  # Mostrando informações do DataFrame limpo
print("---------------------------\n");
dflimpo =dflimpo.assign( ano = dflimpo['ano'].astype(int))
print(dflimpo.info())  # Verificando o tipo de dado da coluna 'ano' após a conversão
print("---------------------------\n");
print(dflimpo.head())  # Mostrando as primeiras linhas do DataFrame limpo após a conversão
print("---------------------------\n");


# Ordenando o gráfico boxplot por salário médio anual (do maior para o menor)
ordem = dflimpo.groupby('experiencia')['salario_usd'].mean().sort_values(ascending=False).index

plt.figure(figsize=(8, 5))
sns.barplot(data=dflimpo, x='experiencia', y='salario_usd', estimator='mean', order=ordem)
plt.title('Salário médio por nível de senioridade')
plt.ylabel('Salário Médio (USD)')
plt.xlabel('Senioridade')
plt.show()
print("---------------------------\n");

plt.figure(figsize=(10, 6))
sns.histplot(data=dflimpo, x='salario_usd', bins=30, kde=True)
plt.title('Distribuição dos Salários Anuais em USD')
plt.xlabel('Salário Anual (USD)')
plt.ylabel('Frequência')
plt.show()
print("---------------------------\n");

plt.figure(figsize=(8, 5))
sns.boxplot(data=dflimpo, x='salario_usd' )
plt.title('Boxplot dos Salários Anuais por Nível de Senioridade')
plt.xlabel('Nível de Senioridade')
plt.ylabel('Salário Anual (USD)')
plt.show()
print("---------------------------\n");

ordem = dflimpo.groupby('experiencia')['salario_usd'].mean().sort_values(ascending=False).index

plt.figure(figsize=(8, 5))
sns.boxplot(data=dflimpo, x='experiencia', y='salario_usd', order=ordem)
plt.title('Boxplot dos Salários Anuais por Nível de Senioridade (ordenado)')
plt.xlabel('Nível de Senioridade')
plt.ylabel('Salário Anual (USD)')
plt.tight_layout()
plt.show()
print("---------------------------\n")


ordem = dflimpo.groupby('experiencia')['salario_usd'].mean().sort_values(ascending=False).index

plt.figure(figsize=(10, 6))
sns.boxplot(
    data=dflimpo,
    x='experiencia',
    y='salario_usd',
    order=ordem,
    palette='Set2'  # Paleta de cores colorida
)
plt.title('Boxplot Colorido dos Salários Anuais por Nível de Experiência')
plt.xlabel('Nível de Experiência')
plt.ylabel('Salário Anual (USD)')
plt.tight_layout()
plt.show()
print("---------------------------\n")

# Gráfico boxplot interativo dos salários por nível de experiência
ordem = dflimpo.groupby('experiencia')['salario_usd'].mean().sort_values(ascending=False).index

fig = px.box(
    dflimpo,
    x='experiencia',
    y='salario_usd',
    category_orders={'experiencia': list(ordem)},
    color='experiencia',
    title='Boxplot Interativo dos Salários Anuais por Nível de Experiência',
    labels={'experiencia': 'Nível de Experiência', 'salario_usd': 'Salário Anual (USD)'}
)
fig.show()


# Função para converter nome do país para ISO-3 usando pycountry
def nome_para_iso3(nome):
    try:
        return pc.countries.lookup(nome).alpha_3
    except:
        return None

# Criar nova coluna com código ISO-3 a partir do nome do país
dflimpo['residencia_iso3'] = dflimpo['residencia'].apply(nome_para_iso3)

# Calcular média salarial por país (ISO-3)
df_ds = dflimpo[dflimpo['cargo'] == 'Data Scientist']
media_ds_pais = df_ds.groupby('residencia_iso3')['salario_usd'].mean().reset_index()

# Gerar o mapa
fig = px.choropleth(
    media_ds_pais,
    locations='residencia_iso3',
    color='salario_usd',
    color_continuous_scale='Viridis',
    title='Salário médio de Cientista de Dados por país',
    labels={'salario_usd': 'Salário médio (USD)', 'residencia_iso3': 'País'}
)

fig.update_geos(showcoastlines=True, showland=True, fitbounds="locations")
fig.show()
dflimpo.head()  # Mostrando as primeiras linhas do DataFrame com a nova coluna
dflimpo.to_csv("salarios_traduzido.csv", index=False)  # Salvando o DataFrame em um novo arquivo CSV    