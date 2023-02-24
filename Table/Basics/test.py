import dash
from dash import Dash, html, dash_table, Input, Output, State
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.P(
            "foobar",
            id='datatable-interactivity-container',
        ),
        dash_table.DataTable(
            id='table',
            # data import
            data=df.to_dict("records"),
            columns=[{"name": i, "id": i} for i in df.columns],
            # table interactivity
            editable=True,
            # filtering=True,
            sort_action="native",
            sort_mode="multi",
            row_selectable="multi",
            # row_deletable=True,
            # table style (ordered by increased precedence: see 
            # https://dash.plot.ly/datatable/style in § "Styles Priority"
            # style table
            style_table={
                'maxHeight': '50ex',
                'overflowY': 'scroll',
                'width': '100%',
                'minWidth': '100%',
            },
            # style cell
            style_cell={
                'fontFamily': 'Open Sans',
                'textAlign': 'center',
                'height': '60px',
                'padding': '2px 22px',
                'whiteSpace': 'inherit',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            },
            style_cell_conditional=[
                {
                    'if': {'column_id': 'State'},
                    'textAlign': 'left'
                },
            ],
            # style header
            style_header={
                'fontWeight': 'bold',
                'backgroundColor': 'white',
            },
            # style filter
            # style data
            style_data_conditional=[
                {
                    # stripped rows
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(248, 248, 248)'
                },
                {
                    # highlight one row
                    'if': {'row_index': 4},
                    "backgroundColor": "#3D9970",
                    'color': 'white'
                }
            ],
        ),
    ]
)



if __name__ == '__main__':
    app.run_server(debug=True)