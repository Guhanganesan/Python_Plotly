# Python_Plotly Setup
1. pip install dash
2. pip install jupyter-dash
3. pip install pandas


# Run 

Drive:\MyFolder\Python_Plotly> python test.py   
Dash is running on http://127.0.0.1:8050/   

 * Serving Flask app 'test'
 * Debug mode: on

# Reference

# 1. Dash HTML
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# 2. Dash CSS
style={'': ''}

# 3. Dash Image
def b64_image(image_filename)
    '''Encode jpg/png image into base64 img'''
    with open(image_filename, 'rb') as file:
        image = file.read()
    return 'data:image/png;base64'+base64.b64encode(image).decode('utf-8')

# 4. Dash APP
app = dash.Dash(__name__,
    server=server,
    external_stylesheets=[dbc.themes.BOOTSTRAP, ],
    external_scripts=)

# Dash Callback

@app.callback(Output('output_id', 'output_prop'), 
            Input('input_id', 'input_prop'))
def fn(input_prop):
    return 

Link: https://dash.plotly.com/basic-callbacks

# 5. Dash Callback with State
@app.callback(Output('output_id', 'output_prop'), 
            Input('input_id', 'input_prop'),
            State('state_id', 'state_prop'))
def fn(input_prop, state_prop):
    return

# 6. Run Dash 
if __name__ == '__main__':
    app.run_server(debug=True, port=)