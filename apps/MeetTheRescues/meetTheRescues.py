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
                html.H1("Find your New Bestfur-iend!"),
                html.Div(
                    [
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src="assets/White.png",
                                    top=True,
                                    style={"opacity": 0.3},
                                    ),
                                dbc.CardImgOverlay(
                                    dbc.CardBody(
                                        [
                                            html.H4("Card title", className="card-title"),
                                            html.P(
                                                "An example of using an image in the background of "
                                                "a card.",
                                                className="card-text",
                                            ),
                                            dbc.Button("Go somewhere", color="primary"),
                                        ],
                                    ),
                                ),
                            ],
                            style={"width": "18rem"},
                        ),

                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src="assets/White.png",
                                    top=True,
                                    style={"opacity": 0.3},
                                    ),
                                dbc.CardImgOverlay(
                                    dbc.CardBody(
                                        [
                                            html.H4("Card title", className="card-title"),
                                            html.P(
                                                "An example of using an image in the background of "
                                                "a card.",
                                                className="card-text",
                                            ),
                                            dbc.Button("Go somewhere", color="primary"),
                                        ],
                                    ),
                                ),
                            ],
                            style={"width": "18rem"},
                        )
                    ]
                )
            ]
        ),
        html.Div(
            [
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
                html.P("[INTRO ABOUT THE PETS WE HAVE AND HOW MANY ARE RESCUED ETC]"),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
                html.P("[DETAILS ABOUT THE SHELTERS]")
            ]
        )
    ]
)
