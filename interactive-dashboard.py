import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Carregar dados
df = pd.read_csv('crimes_intolerancia_tratados.csv')

# Inicializar app Dash
app = dash.Dash(__name__)

# Layout do app
app.layout = html.Div(children=[
    html.H1(children='Mapa de Crimes de Intolerância Religiosa'),
   
    dcc.Graph(
        id='mapa-crimes',
        figure=px.choropleth(df,
                             locations='state',
                             locationmode='country names',
                             color='cases',
                             title='Crimes por Estado no Brasil')
    )
])

# Executar o app
if __name__ == '__main__':
    app.run_server(debug=True)