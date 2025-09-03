# Import my dash library
from dash import Dash, html

# Create my dash app
app = Dash(__name__)
app.title = "Tai Dash App"

# Define the layout of the app
app.layout = html.Div([
    html.H1('Hello Dash', style = {'color': '#381D5C',
                                   'fontSize': '150px',
                                   'backgroundColor': '#E898AA'}),
    html.P('This is a simple dashboard.', style = {'border': '10px solid blue',
                                                   'padding': '50px',
                                                   'margin': '100px'}),
    html.Br(),
    html.A('Click here', href = 'https://www.linkedin.com/feed/'),
    html.P("I'm hungry!")
])

# Run the app
if __name__ == "__main__":
    app.run(debug = True, use_reloader = False)