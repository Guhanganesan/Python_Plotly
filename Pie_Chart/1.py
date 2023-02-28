import dash 
from dash import Dash, html, dcc
import plotly.express as px
import numpy
import dash_bootstrap_components as dbc 
 
# Random Data
random_x = [100, 2000, 550]
names = ['A', 'B', 'C']

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
                        dcc.Graph(
                            id="my_graph",
                            figure=px.pie(values=random_x, names=names)
                        )
                    ]
                )
            ]
        )
    ]
    
)


if __name__ == '__main__':
    app.run(debug=True)