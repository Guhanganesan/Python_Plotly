import dash
from dash import Dash, html, Input, Output, dcc 
import dash_bootstrap_components as dbc 
import pandas as pd 
import plotly.express as px 

df = pd.read_csv("../Web/Bootstrap/mystocks.csv")
#print(df[:15]) #only 15 records
df = df[:15]
print(df.columns) # only columns

"""
0   2022-05-06    AMZN  114.7720  119.0510  113.0810  114.8500  1.242599e+08
1   2022-05-06   GOOGL  115.7460  117.5710  114.0160  115.1840  3.970958e+07
2   2022-05-06     PFE   47.8586   48.0293   46.8827   46.9315  2.038246e+07
3   2022-05-06    BNTX  134.8770  139.9580  132.3510  139.4530  1.417457e+06
4   2022-05-06    MRNA  134.4000  140.6000  131.0000  139.7000  7.013011e+06
5   2022-05-09    AMZN  108.7890  114.0000  107.9570  111.3120  1.281244e+08
6   2022-05-09   GOOGL  112.5110  115.0770  112.0010  113.2500  4.080286e+07
7   2022-05-09     PFE   47.4683   47.9855   46.6192   47.2145  2.562979e+07
8   2022-05-09    BNTX  138.9870  144.7420  137.1840  138.2440  2.553163e+06
9   2022-05-09    MRNA  135.8000  141.6526  131.7800  132.7900  9.625849e+06
10  2022-05-10    AMZN  108.8590  112.6420  107.1710  111.2500  1.054338e+08
11  2022-05-10   GOOGL  114.3950  116.2500  112.9010  115.5080  3.990038e+07
12  2022-05-10     PFE   48.2977   48.6979   47.5122   47.8586  2.801069e+07
13  2022-05-10    BNTX  143.0580  145.8610  137.9770  138.0160  2.281179e+06
14  2022-05-10    MRNA  132.3200  139.0550  127.6100  137.4000  8.180204e+06
"""

app = dash.Dash(__name__)

app.layout = html.Div(
    id="title",
    children=[
        html.H1("Hello"),
        dcc.Dropdown(
            id="my_dpdn",
            options=[
                {"label":x, "value":x} for x in df.Symbols
            ]
        ),
        html.Div(
           dcc.Graph(
            id="my_graph",
            figure={},
            style={"width":"500px"}
           )
        )
    ],
    style={
        "width":"200px"
    }
)

@app.callback(
    Output(
        "my_graph", "figure"
    ),
    Input(
        "my_dpdn", "value"
    )
)
def get_dropdown_value(value):
    print(value)
    """ 
    In different date AMZN has some values that will be displayed in a graph 
    Select brand = AMZN
    x=Date
    y=High
    """

    dff = df[df["Symbols"]==value]
    print(dff['level_0']) # selected value related rows stored in a list
    graph_pie = px.pie(values=dff['High'], names=dff['Symbols'])
    return graph_pie 

if __name__ == '__main__':
    app.run(debug=True)
