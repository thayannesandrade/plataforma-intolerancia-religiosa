import pandas as pd

# Função para carregar dados de fontes públicas
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Dados carregados com sucesso!")
        return df
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return None

# Função para tratar dados (remover nulos e duplicatas)
def clean_data(df):
    df_clean = df.dropna().drop_duplicates()
    print("Dados limpos: nulos e duplicatas removidos.")
    return df_clean

# Função para filtrar dados relevantes (crimes de intolerância religiosa)
def filter_relevant_data(df):
    filtered_df = df[df['crime_type'] == 'intolerância religiosa']
    print(f"Total de crimes de intolerância religiosa: {len(filtered_df)}")
    return filtered_df

# Exemplo de uso
if __name__ == "__main__":
    # Caminho para o arquivo CSV com dados de crimes
    file_path = 'dados_crimes.csv'
    df = load_data(file_path)
   
    if df is not None:
        df_clean = clean_data(df)
        relevant_data = filter_relevant_data(df_clean)
       
        # Salvar os dados tratados em um novo arquivo CSV
        relevant_data.to_csv('crimes_intolerancia_tratados.csv', index=False)
