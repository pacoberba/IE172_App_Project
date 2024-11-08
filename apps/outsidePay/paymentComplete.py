import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

from app import app
from apps.adopt import adopt

# instead of app.layout, we just use the variable "layout" here
# We cannot really modify the "app" variable here, we only do it in index.py
layout = html.Div(
    [
        dbc.Row(
        dbc.Col(html.A("HOME", href="/home", className="back-link"), width="auto"),
        className="back-row"
    ),
    dbc.Row(
        dbc.Col(html.H1("PAYMENT COMPLETE", className="text-warning text-center"), className="title-row"),
    ),
    dbc.Row(
        dbc.Col([
            html.P("Hi Hooman! Your adoption application process or donation transaction has now been successfully completed!" 
                   "You will be receiving email notifications from us regarding Sponsorship renewals and an e-certificate" 
                   "for your kind act (for donations).", className="text-center"),

        ]),
    ),
    html.P(
                    "Thank you for making a difference to the lives of our bestfur-iends, Pawssion Project Fur Parent! 🙂",
                    className="text-center font-weight-bold",
    ),
], className="p-4")