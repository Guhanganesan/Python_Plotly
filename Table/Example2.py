import dash
from dash import html, Input, Output, dash_table, State

app = dash.Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        id='data_table',
        columns=[{
            'name': 'Column {}'.format(i), #column Name
            'id': 'column-{}'.format(i), 
        } for i in range(1, 5)], #4 columns
        data=[
        {'column-{}'.format(i): (j + (i-1)*5) for i in range(1, 5)}
        for j in range(5)
        ],
        style_data={
            'color':'red'
        }
    ),
    html.Div(id='output_div')
])

@app.callback(
    Output('output_div', 'children'),
    Input('data_table', 'active_cell'),
    State('data_table', 'data')
)
def getActiveCell(active_cell, data):
    if active_cell:
        col = active_cell['column_id']
        row = active_cell['row']
        cellData = data[row][col]
        return html.P(f'row: {row}, col: {col}, value: {cellData}')
    return html.P('no cell selected')

if __name__ == '__main__':
    app.run_server(debug=True)