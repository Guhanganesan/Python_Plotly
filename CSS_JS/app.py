import dash
from dash import Dash, html, dcc

app = Dash(
    __name__,
    # List of urls
    external_scripts=['./assets/js/test.js'],
    external_stylesheets=['./assets/css/header.css', './assets/css/example.css']
    )

app.layout = html.Div([
    html.Div(
        className="app-header",
        children=[
            html.Div('Plotly Dash', className="app-header--title")
        ]
    ),
    html.Div(
        children=html.Div([
            html.H5('Overview'),
            html.Div( 
            className='example_class',
            children=['''
                This is an example of a simple Dash app with
                local, customized CSS.
            '''])
        ])
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)


"""
https://dash.plotly.com/external-resources

There are a few things to keep in mind when including assets automatically:

1 - The following file types will automatically be included:

A - CSS files suffixed with .css

B - JavaScript files suffixed with .js

C - A single file named favicon.ico (the page tab's icon)

2 - Dash will include the files in alphanumerical order by filename. So, we recommend prefixing your filenames with numbers if you need to ensure their order (e.g. 10_typography.css, 20_header.css)

3 - You can ignore certain files in your assets folder with a regex filter using app = dash.Dash(assets_ignore='.*ignored.*'). This will prevent Dash from loading files which contain the above pattern.

4 - If you want to include CSS from a remote URL, then see the next section.

5 - Your custom CSS will be included after the Dash component CSS

6 - It is recommended to add __name__ to the dash init to ensure the resources in the assets folder are loaded, eg: app = dash.Dash(__name__, meta_tags=[...]). When you run your application through some other command line (like the flask command or gunicorn/waitress), the __main__ module will no longer be located where app.py is. By explicitly setting __name__, Dash will be able to locate the relative assets folder correctly.
"""
