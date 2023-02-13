from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Welcome to Plotly'),
    html.P("Plotly html tags")
])

app.run_server(debug=True)