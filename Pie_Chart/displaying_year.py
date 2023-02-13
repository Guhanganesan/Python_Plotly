import dash 
import dash_core_components as dcc
import dash_html_components as html 
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

df1 = pd.read_csv('Data 4.0.csv')
years = df1['Yield Year'].unique()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.Label(['Audit Yield']),
        dcc.Dropdown(
            id='my_dropdown',
            options=[{'label': y, 'value': y} for y in years],
            value=years[0],
            multi=False,
            clearable=False,
            style={"width": "50%"}
        )
    ]),

    html.Div([
        dcc.Graph(id='the_graph')
    ]),

])


@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)
def update_graph(year):
    piechart = px.pie(
        df1[df1['Yield Year'] == int(year)],
        values='Amount',
        names='Status',
        hole=.3,
    )
    return piechart


if __name__ == '__main__':
    app.run_server()