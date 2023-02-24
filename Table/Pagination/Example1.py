import dash
from dash import html, dcc, Input, Output, dash_table
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
df[' index'] = range(1, len(df) + 1)    
app = dash.Dash(__name__)    
PAGE_SIZE = 8    

app.layout = html.Div([    
    html.Div('Data table pagination test'),    
    dcc.Dropdown(    
        id='select_page_size',    
        options=[{'label': '5', 'value': 5}, {'label': '10', 'value': 10}, {'label': '15', 'value': 15}],    
        value=5    
    ),    
    html.Div(dash_table.DataTable(    
        id='datatable-paging',    
        columns=[{"name": i, "id": i} for i in df.columns],    
        data=df.to_dict("records"),    
        page_size=PAGE_SIZE,    
        page_current=0,    
    ))    
])        

@app.callback(    
    Output('datatable-paging', 'page_size'),    
    [Input('select_page_size', 'value')])   # pass value to page_size
def update_graph(page_size):    
    return page_size

    
if __name__ == '__main__':    
    app.run_server(debug=True)