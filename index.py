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
from apps.register import register
from apps.signIn import signIn
#from apps.headnfootTemplate import create_footer

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        hft.create_header(),
        dcc.Location(id='url', refresh=True),
        html.Div(id='page_content'),
        hft.create_footer()
    ],
    style={
        'display': 'flex',
        'flexDirection': 'column', 
        'height': '100vh',          
        'justifyContent': 'space-between',
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
            returnlayout = signIn.layout

        elif pathname == '/register':
            returnlayout = register.layout

        else:
            returnlayout = 'error404'
    
    else: 
        raise PreventUpdate
    
    return [returnlayout]

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8050/', new=0, autoraise=True)
    app.run_server(debug=False)
