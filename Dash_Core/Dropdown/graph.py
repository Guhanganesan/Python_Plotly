from dash import Dash, dcc, html
import plotly.express as px

app = Dash(__name__)

df = px.data.iris()  # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")

app.layout = html.Div([
dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)