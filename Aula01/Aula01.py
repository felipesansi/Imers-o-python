import pandas as pd

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
    # Adicione outros conforme necessário
}

# Aplicando as traduções
df['experiencia'] = df['experiencia'].map(mapa_experiencia)
df['tipo_emprego'] = df['tipo_emprego'].map(mapa_tipo_emprego)
df['porte_empresa'] = df['porte_empresa'].map(mapa_porte_empresa)
df['residencia'] = df['residencia'].map(mapa_paises)
df['local_empresa'] = df['local_empresa'].map(mapa_paises)

# Agora sim, os prints mostrarão os valores traduzidos
print(df['experiencia'].value_counts())
print("---------------------------\n")
print(df['porte_empresa'].value_counts())
print("---------------------------\n")
print(df['tipo_emprego'].value_counts())
print("---------------------------\n")
print(df['residencia'].value_counts())
print("---------------------------\n")
print(df['local_empresa'].value_counts())
print("---------------------------\n")
print(df.head())
print("---------------------------\n")
print(df.describe (include='object'))