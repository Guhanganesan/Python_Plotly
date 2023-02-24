from dash import Dash, html, dash_table, Input, Output, State
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

app = Dash(__name__)

app.layout = html.Div(
    [ # Add List of items here if it is more than one to be used...
        dash_table.DataTable(
        id="input_table",
        data=df.to_dict('records'), 
        columns=[{"name": i, "id": i} for i in df.columns],
        # Using CSS for the table

        style_table={
                'maxHeight': '50ex',
                'overflowY': 'scroll',
                'width': '100%',
                'minWidth': '100%',
        },

        style_data={
            'color':'blue',
            'text-align':'center',
            'background-color':'pink',
            'font-size':'14px',
            'font-family':'arial',
            'border':'1px solid black'
        },
        
        # style_cell={
        #     'color':'blue', # entire table text
        #     'text-align':'center', # entire table
        #     'background-color':'pink', # entire table
        #     'width':'100px',
        #     'border':'2px solid blue', #entire table
        #     'height':'60px', # entire table
        # },

        style_header={
            'background-color':'green',
            'color':'white',
            'text-align':'center'
        },
        
        style_header_conditional=[
            {
                'if': {'column_id':'State'},
                'width':'80px'
            },
            {
                'if': {'column_id':'Number of Solar Plants'},
                'width':'80px'
            },
            {
                'if':{'column_id':'Installed Capacity (MW)'},
                'width':'100px'
            },
            {
                'if':{'column_id':'Average MW Per Plant'},
                'width':'80px'
            }
        ],

        style_data_conditional=[
            {
                'if':{'column_id':'Number of Solar Plants'},
                'background-color':'yellow'
            },
            {
                'if':{'column_id':'Average MW Per Plant'},
                'background-color':'blue',
                'color':'white'
            },
            {
                'if': {'row_index': 4},
                "backgroundColor": "#3D9970",
                'color': 'white'
            },
            {
                'if': { 'column_id': 'Generation (GWh)', 'filter_query': '{{Generation (GWh)}} = {}'.format(2550)},
                'background-color':'red',
                'color':'white'
            }
            
        ]

        ),
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)

"""
Valid keys: [
        "column_id",
        "column_type",
        "header_index",
        "column_editable"
        ]
""",