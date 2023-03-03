from dash import Dash, html, dcc, Input, Output, dash_table
from dash.exceptions import PreventUpdate

import collections
import pandas as pd


app = Dash(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

"""
CSV Data:
country,        year,   pop,    continent,lifeExp,gdpPercap
Afghanistan,1952,8425333,Asia,28.801,779.4453145
Afghanistan,1957,9240934,Asia,30.332,820.8530296
Afghanistan,1962,10267083,Asia,31.997,853.10071
Afghanistan,1967,11537966,Asia,34.02,836.1971382
Afghanistan,1972,13079460,Asia,36.088,739.9811058
Afghanistan,1977,14880372,Asia,38.438,786.11336
Afghanistan,1982,12881816,Asia,39.854,978.0114388
"""

app.layout = html.Div([
    dcc.Store(id='memory-output'),
    dcc.Dropdown(df.country.unique(),
                 ['Canada', 'United States'], # default
                 id='memory-countries',
                 multi=True),
    dcc.Dropdown({'lifeExp': 'Life expectancy', 'gdpPercap': 'GDP per capita'},
                 'lifeExp',
                 id='memory-field'),
    html.Div([
        dcc.Graph(id='memory-graph'),
        dash_table.DataTable(
            id='memory-table',
            columns=[{'name': i, 'id': i} for i in df.columns]
        ),
    ])
])


@app.callback(Output('memory-output', 'data'),
              Input('memory-countries', 'value'))
def filter_countries(countries_selected):
    if not countries_selected:
        # Return all the rows on initial load/no country selected.
        return df.to_dict('records')

    filtered = df.query('country in @countries_selected')

    return filtered.to_dict('records')


@app.callback(Output('memory-table', 'data'),
              Input('memory-output', 'data'))
def on_data_set_table(data):
    if data is None:
        raise PreventUpdate

    return data


@app.callback(Output('memory-graph', 'figure'),
              Input('memory-output', 'data'),
              Input('memory-field', 'value'))
def on_data_set_graph(data, field):
    if data is None:
        raise PreventUpdate

    aggregation = collections.defaultdict(
        lambda: collections.defaultdict(list)
    )

    for row in data:

        a = aggregation[row['country']]

        a['name'] = row['country']
        a['mode'] = 'lines+markers'

        a['x'].append(row[field])
        a['y'].append(row['year'])

    return {
        'data': [x for x in aggregation.values()]
    }


if __name__ == '__main__':
    app.run_server(debug=True, threaded=True)