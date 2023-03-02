import dash 
from dash import Dash, dcc, html 
from plotly.express import data
import pandas as pd

df =  data.medals_long()

app = Dash(__name__)

app.layout = dcc.RadioItems(
    [
        {
            "label": html.Div(['Montreal'], style={'color': 'Gold', 'font-size': 20}),
            "value": "Montreal",
        },
        {
            "label": html.Div(['NYC'], style={'color': 'MediumTurqoise', 'font-size': 20}),
            "value": "NYC",
        },
        {
            "label": html.Div(['London'], style={'color': 'LightGreen', 'font-size': 20}),
            "value": "London",
        },
    ], value='Montreal'
)

if __name__ == "__main__":
    app.run_server(debug=True)
