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
        style_data={
            'color':'blue',
            'text-align':'center',
            'background-color':'pink',
            'font-size':'14px',
            'font-family':'arial'
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