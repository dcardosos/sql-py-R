#TODO: pegar os dados de fraudes do case da paypal e trazer pra dentro
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from sql_tools import SQL
from graphs import Graphs

query1 = """
    SELECT t1.species as species, count(*) as qtd_of_penguins
    FROM penguins t1 
    GROUP BY t1.species
    """

query2 = """
    SELECT t1.island as island, count(*) as qtd_of_penguins
    FROM penguins t1 
    GROUP BY t1.island
"""
    
sql_obj = SQL()
result1 = sql_obj.make_query(query1)
result2 = sql_obj.make_query(query2)

dash_obj = Graphs()

qtd_by_specie = dash_obj.barplot( 
    df = result1,
    x = 'qtd_of_penguins',
    y = 'species',
    title = 'Quantity of penguins',
    color = 'species')

qtd_by_island = dash_obj.barplot(
    df = result2, 
    x = 'qtd_of_penguins',
    y = 'island',
    title = 'Quantity of penguins',
    color = 'island')

app = dash.Dash(__name__)

app.layout = html.Div(children = [
    html.H1('Simple barplot'),
    html.H2('Using `penguins` dataset'),
    dcc.Graph(id = 'by-specie-plot', figure = qtd_by_specie),
    dcc.Graph(id = 'by-island-penguins', figure = qtd_by_island)
])

if __name__ == '__main__':
    app.run_server(debug=True, port = 8050)