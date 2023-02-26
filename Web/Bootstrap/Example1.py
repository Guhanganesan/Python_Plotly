import dash 
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc  
import plotly.express as px
import pandas as pd 
import pandas_datareader.data as web
import datetime 

# start = datetime.datetime(2022,5,6)
# print(start)
# end = datetime.datetime(2022,7,6)
# print(end)

# df = web.DataReader(['AMZN','GOOGL','FB','PFE','BNTX','MRNA'], 'stooq', start=start, end=end)

# df = df.stack().reset_index()
# print(df[:15])

#convert into csv
#df.to_csv("mystocks.csv", index=False)

# Read CSV
df = pd.read_csv("mystocks.csv")
print(df[:15])

app = dash.Dash(__name__,
    # server=server,
    external_stylesheets=[dbc.themes.BOOTSTRAP, ],
    meta_tags=[
        {'name':'view_port',
          'content':'width=device-width, initial-scale=1.0'
        }
    ]
    )

app.layout = dbc.Container([
    # https://hackerthemes.com/bootstrap-cheatsheet/
    dbc.Row([
        dbc.Col([
            html.H1(
                "Stock Market Dashboard",
                className="text-center text-white bg-success mb-4")
        ],
        # Allowed arguments: align, children, className, class_name, id, key, lg, 
        # loading_state, md, sm, style, width, xl, xs, xxl
        sm=12)
    ]),

    dbc.Row([
        # First Columns
        dbc.Col([
           dcc.Dropdown(
                id='my-dpdn', 
                className='',
                options=[{'label':x, 'value':'x'} for x in sorted(df['Symbols'].unique()) ],
                value='AMZN',
                #placeholder='',
                multi=False,
            ),
            dcc.Graph(
                id='line-fig',
                figure={}
            )
        ],
        # width={'size':5, 'offset':1, 'order':1},
        xs=12, sm=12, md=12, lg=5, xl=5
        ),

        # Second Column
        dbc.Col([
            dcc.Dropdown(
                id='my-dpdn2', 
                multi=True, 
                value=['PFE','BNTX'],
                options=[{'label':x, 'value':x}
                                  for x in sorted(df['Symbols'].unique())],
                ),
            dcc.Graph(id='line-fig2', figure={})
        ], 
        #width={'size':5, 'offset':0, 'order':2},
        xs=12, sm=12, md=12, lg=5, xl=5,
        # no_gutters=True => not allowed
        style={"justify":"start"}, # start, center, end, between, around
        )

    ]),

    # Third Row
    dbc.Row([
        dbc.Col([
            html.P(
                "Please select stock",
                style={"text-decoration":"underline"}
                ),
            dcc.Checklist(
                id="my-checklist",
                value=["FB", "GOOGL","AMZN"],
                options=[{'label':x, 'value':x}
                                for x in sorted(df['Symbols'].unique())],
                #Allowed arguments: 
                #className, id, inline, inputClassName, inputStyle, 
                #labelClassName, labelStyle, loading_state, 
                #options, persisted_props, persistence, persistence_type, style, value
                labelClassName="mr-5 text-success"
            ),
            #Allowed arguments: animate, animation_options, className, clear_on_unhover, clickAnnotationData, 
            #clickData, config, extendData, figure, hoverData, id, loading_state, mathjax, prependData, relayoutData,
            #responsive, restyleData, selectedData, style
            dcc.Graph(
                id="my-hist",
                figure={}
            )
        ],
        width={'size':5, 'offset':0},
        style={"justify":"start"},
    )


    ])

],
className="bg-light",
fluid=True
)


# Callback section: connecting the components
# ************************************************************************
# Line chart - Single
@app.callback(
    Output('line-fig', 'figure'),
    Input('my-dpdn', 'value')
)
def update_graph(stock_slctd):
    dff = df[df['Symbols']==stock_slctd]
    figln = px.line(dff, x='level_0', y='High')
    return figln


# Line chart - multiple
@app.callback(
    Output('line-fig2', 'figure'),
    Input('my-dpdn2', 'value')
)
def update_graph(stock_slctd):
    dff = df[df['Symbols'].isin(stock_slctd)]
    figln2 = px.line(dff, x='level_0', y='Open', color='Symbols')
    return figln2


# Histogram
@app.callback(
    Output('my-hist', 'figure'),
    Input('my-checklist', 'value')
)
def update_graph(stock_slctd):
    dff = df[df['Symbols'].isin(stock_slctd)]
    dff = dff[dff['level_0']=='2022-05-06']
    fighist = px.histogram(dff, x='Symbols', y='Close')
    return fighist

#Thanks: https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Bootstrap/Complete_Guide/live_bootstrap.py

if __name__ == '__main__':
    app.run_server(debug=True)



