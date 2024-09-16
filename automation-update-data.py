import requests
import pandas as pd

# Função para buscar dados de uma API pública
def fetch_data_from_api(api_url):
    response = requests.get(api_url)
   
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['results'])  # Converter dados em DataFrame
        return df
    else:
        print("Erro ao acessar API")
        return None

# Exemplo de uso
if __name__ == "__main__":
    api_url = 'https://api.gov.br/dados-intolerancia-religiosa'
    df = fetch_data_from_api(api_url)
   
    if df is not None:
        df.to_csv('novos_dados.csv', index=False)
        print("Novos dados salvos com sucesso!")