import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

from app import app

# instead of app.layout, we just use the variable "layout" here
# We cannot really modify the "app" variable here, we only do it in index.py
layout = html.Div(
    [
        html.H1("Enter User Credentials"),
        html.Div(
            [
                dbc.Label("Email", html_for="example-email"),
                dbc.Input(type="email", id="example-email", placeholder="Enter email"),
                dbc.FormText(
                    "Are you on email? You simply have to be these days",
                    color="secondary",
                ),
            ],
            className="mb-3",
        ),
        html.Div(
            [
                dbc.Label("Email", html_for="example-email"),
                dbc.Input(type="email", id="example-email", placeholder="Enter email"),
                dbc.FormText(
                    "Are you on email? You simply have to be these days",
                    color="secondary",
                ),
                dbc.Button("Register", color='dark', href="/register", style={'margin': '0 10px'}),
                dbc.Row(
                    [
                        html.P("Don’t have an account?"),
                        html.Label(['Sign Up', html.A('link', href='/register')])
                    ]
                )
            ],
            className="mb-3",
        )
    ],
)
