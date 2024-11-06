import webbrowser

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# Importing your app variable from app.py so we can use it
from app import app
from apps import headnfootTemplate as hft
from apps import home
from apps.adopt import adopt
from apps.companyInfo import contactUs, faqs, ourStory
from apps.donate import donate
from apps.MeetTheRescues import meetTheRescues
#from apps.headnfootTemplate import create_footer

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

#print(create_header())
a = 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur'

app.layout = html.Div(
    [
        hft.create_header(),
        dcc.Location(id='url', refresh=True),
        html.Div(
            children=[
                html.H1("Welcome to Pawssion Project"),
                html.P(a),
                html.P(a),
            ],
            style={
                'position':'relative',             # Allow content to take up remaining space
                'marginTop': '150px',  # Give space for the fixed header (adjust based on header height)
                'padding': '60px'
            }
        ),
        hft.create_footer()
    ],
    style={
        'display': 'flex',              # Use Flexbox to structure the layout
        'flexDirection': 'column',      # Stack the header and footer vertically
        'height': '100vh',              # Ensure the layout takes up the full viewport height
        'justifyContent': 'space-between',  # Push the header and footer to top and bottom
    }
)

@app.callback(
    [
        Output('page_content', 'children')
    ],
    [
        Input('url', 'pathname')
    ]
)
def displaypage (pathname):
    
    # This code block extracts the id of the triggered input
    ctx = dash.callback_context
    if ctx.triggered:
        eventid = ctx.triggered[0]['prop_id'].split('.')[0]   
    else:
        raise PreventUpdate

        
    # This code block executes action based on the value of eventid
    if eventid == 'url':
        if pathname == '/' or pathname == '/home':
            returnlayout = home.layout

        elif pathname == '/adopt':
            returnlayout = adopt.layout
        
        elif pathname == '/donate':
            returnlayout = donate.layout

        elif pathname == '/meettherescues':
            returnlayout = meetTheRescues.layout

        elif pathname == '/ourstory':
            returnlayout = ourStory.layout

        elif pathname == '/faqs':
            returnlayout = faqs.layout

        elif pathname == '/contactus':
            returnlayout = contactUs.layout
        
        elif pathname == '/signin':
            returnlayout = 'signin'

        elif pathname == '/register':
            returnlayout = 'register'

        else:
            returnlayout = 'error404'
    
    else: 
        raise PreventUpdate
    
    return [returnlayout]

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8050/', new=0, autoraise=True)
    app.run_server(debug=False)
