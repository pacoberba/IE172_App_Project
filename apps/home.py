import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

from app import app

# instead of app.layout, we just use the variable "layout" here
# We cannot really modify the "app" variable here, we only do it in index.py
layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    html.Img(src="assets/DSC_2895-scaled.jpg",
                             style={'width': '100%',
                                    'height': 'auto',
                                    'object-fit': 'cover',
                                    'object-position': 'center',
                                    'width': '1920px',
                                    'height': '500px'}
                                    ),
                                    style={'width': '1920px',
                                           'height': '500px',
                                           'overflow': 'hidden',
                                           }
                ),
                html.Div(
                    [
                        html.Div(
                            html.H1("Join the Pawssion Project!")
                        ),
                        html.Div(
                            html.H2("Our mission is to rescue.")
                        ),
                        html.Div(
                            html.H2("Our mission is to rescue.")
                        ),
                        html.Div(
                            [dbc.Button("Sign-In", color='light', href="/signin", style={'margin': '0 10px'})]
                        )
                    ]
                )
            ]
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.H1("Adopt"),
                        html.P("Many of our Adoptables from our Bulacan and Bacolod Shelters have been rescued from death row, from local pounds or from abusive environments. By choosing to adopt, you are giving them the chance to find a new home and to feel the love and security they deserve.")
                    ]
                ),
                html.Div(
                    [
                        html.H1("Donate"),
                        html.P("As a non-profit organization, Pawssion Project operates and relies heavily on donations from the community. We are always called upon to rescue animals suffering from abandonment, abuse, injury or neglect and none of it is possible without your support.")
                    ]
                )
            ]
        )
    ]
)
