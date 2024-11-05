import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

from app import app

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        html.Header(
            [
                html.Img(
                    src = "assets/PawssionProjectLogo.png",
                    style={
                        'width': '400px',      # Set width to 100% to make it responsive
                        'maxWidth': '400px',  # Optional: limit the max width
                        'height': 'auto',     # Maintain aspect ratio
                        'margin': '20px 0',
                        }
                ),
                dbc.Nav(
                    [
                        html.Div([dbc.Button("Adopt",style={'margin': '0 10px', 'backgroundColor':'#556B2F'})]),
                        dbc.NavItem(dbc.NavLink("Donate", href="#", style={'color':'black'})),
                        dbc.NavItem(dbc.NavLink("Meet the Rescues", href="#", style={'color':'black'})),
                        dbc.NavItem(dbc.NavLink("Our Story",  href="#", style={'color':'black'})),
                        dbc.NavItem(dbc.NavLink("FAQs", href="#", style={'color':'black'})),
                        html.Div([dbc.Button("Sign-In", color='light', href="/signin", style={'margin': '0 10px'})]),
                        html.Div([dbc.Button("Register", color='dark', href="/register", style={'margin': '0 10px'})])
                    ],
                    navbar=True,
                    style={'justifyContent': 'center','display': 'flex','padding':'40px'} 
                )
            ],
            style={
                'position': 'fixed',
                'top': '0',
                'left': '0',
                'right': '0',
                'backgroundColor': '#F7EFCF',  # Header background
                'boxShadow': '0 2px 5px rgba(0,0,0,0.1)',
                'justifyContent': 'center',
                'display': 'flex'
            }
        ),

        html.Footer(
            html.Div(
                [
                    html.P("Pawssion Project Foundation Inc.", style={'textAlign': 'center'}),
                    html.P("Bulacan Shelter: 1429 Paradise 1, Purok 7 Tungkong Mangga, SJDM, Bulacan", style={'textAlign': 'center'}),
                    html.P("Bacolod Shelter: Balay Pawssion, Google Maps: M2JV+5W, Bacolod, Negros Occidental", style={'textAlign': 'center'}),
                    html.P("info@pawssionproject.org", style={'textAlign': 'center'})
                ],
                style={
                    'padding': '20px',
                    'backgroundColor': '#343434',  # Light background color
                    'borderTop': '1px solid #dee2e6',  # Top border for separation
                    'color':'white'
                }
            ),
            style={'marginTop': 'auto'}
        )
    ],
    style={'display': 'flex', 'flexDirection': 'column', 'minHeight': '100vh'}
)
