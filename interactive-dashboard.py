import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px


df = pd.read_csv('crimes_intolerancia_tratados.csv')

df_grouped = df.groupby('Estado').size().reset_index(name='quantidade_crime')


app = dash.Dash(__name__)


app.layout = html.Div(children=[
    html.H1(children='Mapa de Crimes de Intolerância Religiosa'),
   
    dcc.Graph(
        id='mapa-crimes',
        figure=px.choropleth(df_grouped,
                             locations='Estado',
                             locationmode='country names',
                             color='quantidade_crime',
                             title='Crimes por Estado no Brasil',
                             labels={'quantidade_crime': 'Número de Crimes'}
        )
    )
])

# Executar o app
if __name__ == '__main__':
    app.run_server(debug=True)