import dash 
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, html

app = dash.Dash(__name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {'name':'view_port',
          'content':'width=device-width, initial-scale=1.0'
        }
    ]
)

app.layout =  html.Div(
    [
        dbc.Button(
            "Open collapse",
            id="collapse-button",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody("This content is hidden in the collapse")),
            id="collapse",
            is_open=False,
        ),
    ]
)

# Ref: https://dash-bootstrap-components.opensource.faculty.ai/docs/components/collapse/

@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

    
if __name__ == '__main__':
    app.run_server(debug=True)