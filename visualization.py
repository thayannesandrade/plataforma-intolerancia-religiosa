import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Função para gerar gráficos estáticos com Matplotlib
def plot_static_data(df):
    plt.figure(figsize=(10, 6))
    df['state'].value_counts().plot(kind='bar', color='blue')
    plt.title('Casos de Intolerância Religiosa por Estado')
    plt.xlabel('Estado')
    plt.ylabel('Número de Casos')
    plt.show()

# Função para gerar visualizações interativas com Plotly
def plot_interactive_data(df):
    fig = px.choropleth(df,
                        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson',
                        locations='state',
                        color='cases',
                        hover_name='state',
                        title='Mapa Interativo de Crimes de Intolerância Religiosa no Brasil')
    fig.update_geos(fitbounds="locations", visible=False)
    fig.show()

# Exemplo de uso
if __name__ == "__main__":
    # Carregar os dados tratados
    df = pd.read_csv('crimes_intolerancia_tratados.csv')
   
    # Gerar gráficos estáticos e interativos
    plot_static_data(df)
    plot_interactive_data(df)