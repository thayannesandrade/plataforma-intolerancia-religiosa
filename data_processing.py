import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path, usecols=['Bairro', 'Estado', 'Descrição', 'tipo_crime'])
        print("Dados carregados com sucesso!")
        return df
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return None


def clean_data(df):

    df['tipo_crime'] = df['tipo_crime'].str.strip()

    df_clean = df.dropna().drop_duplicates()
    print("Dados limpos: nulos e duplicatas removidos.")
    return df_clean


def filter_relevant_data(df):
    filtered_df = df[df['tipo_crime'] == 'racismo religioso']
    print(f"Total de crimes de intolerância religiosa/racismo religioso: {len(filtered_df)}")
    return filtered_df

# Exemplo de uso
if __name__ == "__main__":
    file_path = 'dados_crimes.csv'
    df = load_data(file_path)
   
    if df is not None:
        df_clean = clean_data(df)
        relevant_data = filter_relevant_data(df_clean)
       
        relevant_data.to_csv('crimes_intolerancia_tratados.csv', index=False)
