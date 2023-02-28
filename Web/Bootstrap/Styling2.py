import dash 
from dash import Dash, html, dcc
import plotly.express as px
import numpy
import dash_bootstrap_components as dbc 
 

app = dash.Dash(__name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, ],
    meta_tags=[
        {'name':'view_port',
          'content':'width=device-width, initial-scale=1.0'
        }
    ]
)

app.layout = html.Div(
    className="container",
    children=[
       html.Div(
            className="row",
            children=[
                html.Div(
                    className="col-sm-12",
                    children=[
                        # https://dashcheatsheet.pythonanywhere.com/
                        # border-top, border-bottom, border-end, border-start, border-3, border-end-5
                        # border-danger 
                        # border rounded, rounded-top, rounded-end, rounded-bottom
                        # rounded-start, rounded-circle, rounded-pill
                        html.Div(
                            className="border border-3 border-top-8 border-danger bg-success", 
                            style={"height":"30px"}
                        ),
                        html.Br(),
                        # Text 
                        html.P("text-primary", className="text-primary"),
                        html.P("text-secondary", className="text-secondary"),
                        html.P("text-success", className="text-success"),
                        html.P("text-danger", className="text-danger"),
                        html.P("text-warning", className="text-warning"),
                        html.P("text-info", className="text-info"),
                        html.P("text-light", className="text-light"),
                        html.P("text-dark", className="text-dark")

                        html.Br(),
                        
                        # Gutters: https://getbootstrap.com/docs/5.0/layout/gutters/
                        # Align Items start, center, end : https://getbootstrap.com/docs/5.0/layout/columns/
                        
                    ]
                )
            ]
        ),
    ]
    
)


if __name__ == '__main__':
    app.run(debug=True)