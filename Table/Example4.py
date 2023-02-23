from dash import Dash, html, dash_table, Input, Output, State
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

print(df.to_dict('records'))
"""
[
{'State': 'California', 'Number of Solar Plants': 289, 'Installed Capacity (MW)': 4395, 'Average MW Per Plant': 15.3, 'Generation (GWh)': 10826}, 
{'State': 'Arizona', 'Number of Solar Plants': 48, 'Installed Capacity (MW)': 1078, 'Average MW Per Plant': 22.5, 'Generation (GWh)': 2550}, {'State': 'Nevada', 'Number of Solar Plants': 11, 'Installed Capacity (MW)': 238, 'Average MW Per Plant': 21.6, 'Generation (GWh)': 557}, 
{'State': 'New Mexico', 'Number of Solar Plants': 33, 'Installed Capacity (MW)': 261, 'Average MW Per Plant': 7.9, 'Generation (GWh)': 590}, 
{'State': 'Colorado', 'Number of Solar Plants': 20, 'Installed Capacity (MW)': 118, 'Average MW Per Plant': 5.9, 'Generation (GWh)': 235}, {'State': 'Texas', 'Number of Solar Plants': 12, 'Installed Capacity (MW)': 187, 'Average MW Per Plant': 15.6, 'Generation (GWh)': 354}, 
{'State': 'North Carolina', 'Number of Solar Plants': 148, 'Installed Capacity (MW)': 669, 'Average MW Per Plant': 4.5, 'Generation (GWh)': 1162}, 
{'State': 'New York', 'Number of Solar Plants': 13, 'Installed Capacity (MW)': 53, 'Average MW Per Plant': 4.1, 'Generation (GWh)': 84}
]
"""
print(df.columns)
"""
['State', 'Number of Solar Plants', 'Installed Capacity (MW)', 'Average MW Per Plant', 'Generation (GWh)']
"""

app = Dash(__name__)

app.layout = html.Div(
    [ # Add List of items here if it is more than one to be used...
        dash_table.DataTable(
        id="input_table",
        data=df.to_dict('records'), 
        # columns list of dict
        columns=[{"name": i, "id": i} for i in df.columns],
        # style_cell, style_cell_conditional, style_data, style_data_conditional,style_filter
        # style_filter_conditional, style_header, style_header_conditional, style_table
        style_data={
            'border':'1px solid blue',
            'color':'blue',
            'text-align':'center',
            'background-color':'pink',
            'font-size':'14px',
            'font-family':'arial',

        },
        style_header={
            'border':'1px solid blue',
            'color':'white',
            'background-color':'green',
            'text-align':'center'
        }),

        # Display Result Here
        html.Div(
            id="display_output"
        )
    ]
)

@app.callback(
    Output("display_output", "children"),
    Input("input_table", "active_cell"),
    State("input_table", "data")
)
def display(active_cell, data):
    if active_cell:
        col = active_cell['column_id']
        row = active_cell['row']
        cellData = data[row][col]
        return cellData


if __name__ == '__main__':
    app.run_server(debug=True)