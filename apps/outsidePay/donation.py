import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

# Import the app from your main application file (you need to create an `app.py` file with `app = dash.Dash(...)`)
from app import app

# Layout for the payment form
layout = html.Div(
    [
        # Header section
        dbc.Row(
            dbc.Col(html.H1("PAYMENT FORM", className="text-warning text-left", style={'margin-top': '1px'})),
        ),
        
        # Paragraph describing the form
        dbc.Row(
            dbc.Col(html.P("Make a Donation", style={'textAlign': 'left', "font-weight": "bold", "font-family": "Roboto", 'marginBottom': '40px'})),
        ),
        
        # Form and Image Columns in a single Row
        dbc.Row(
            [
                # Form Column
                dbc.Col(
                    [
                        # Type of Donation
                        dbc.Row(dbc.Col(dbc.Label("Type of Donation*", className="mt-3"))),
                        dbc.Row(
                            dbc.Col(
                                dbc.Select(
                                    options=[
                                        {"label": "Option A: I Choose My Rescue/s Donation", "value": "Option A"},
                                        {"label": "Option B: Choose a Rescue for Me Donation", "value": "Option B"},
                                    ],
                                    placeholder="Select Donation Type",
                                    className="mb-3"
                                )
                            )
                        ),
                        
                        # For Option A, indicate rescue/s to sponsor
                        dbc.Row(dbc.Col(dbc.Label("For Option A, indicate rescue/s to sponsor*", className="mt-3"))),
                        dbc.Row(
                            dbc.Col(
                                dbc.Input(type="text", placeholder="Indicate rescue name", className="mb-3")
                            )
                        ),

                        # Frequency of Sponsorship
                        dbc.Row(dbc.Col(dbc.Label("Frequency of Sponsorship*", className="mt-3"))),
                        dbc.Row(
                            dbc.Col(
                                dbc.Select(
                                    options=[
                                        {"label": "Monthly", "value": "Monthly"},
                                        {"label": "Bi-annual", "value": "Bi-annual"},
                                        {"label": "Yearly", "value": "Yearly"},
                                        {"label": "One-Time Only", "value": "One-Time"},
                                    ],
                                    placeholder="Select Frequency",
                                    className="mb-3"
                                )
                            )
                        ),

                        # Mode of Payment
                        dbc.Row(dbc.Col(dbc.Label("Mode of Payment*", className="mt-3"))),
                        dbc.Row(
                            dbc.Col(
                                dbc.Select(
                                    options=[
                                        {"label": "PayPal", "value": "PayPal"},
                                        {"label": "BDO", "value": "BDO"},
                                        {"label": "BPI", "value": "BPI"},
                                        {"label": "UnionBank", "value": "UnionBank"},
                                        {"label": "GCash", "value": "GCash"},
                                        {"label": "PayMaya", "value": "PayMaya"},
                                    ],
                                    placeholder="Select Payment Method",
                                    className="mb-3"
                                )
                            )
                        ),

                        # File Upload
                        dbc.Row(dbc.Col(dbc.Label("Please upload a copy of your proof of payment*", className="mt-3"))),
                        dbc.Row(
                            dbc.Col(
                                dcc.Upload(
                                    id="upload-data",
                                    children=html.Div(["📤 ", html.A("Add File")]),
                                    style={
                                        "width": "100%",
                                        "height": "60px",
                                        "lineHeight": "60px",
                                        "borderWidth": "1px",
                                        "borderStyle": "dashed",
                                        "borderRadius": "5px",
                                        "textAlign": "center",
                                        "marginBottom": "20px",
                                    },
                                    multiple=False
                                )
                            )
                        ),

                        # Footer with Back and Next buttons
                        dbc.Row(
                            dbc.Col(
                                [
                                    dbc.Button("BACK", color="secondary", href='/previous-page', outline=True, className="btn-back mx-1", style={'font-family': 'Roboto', 'margin-top': '10px'}),
                                    dbc.Button("SUBMIT", href="/outsidePay/paymentComplete", className="btn-custom mx-1", style={'font-family': 'Roboto', 'margin-top': '10px'})
                                ],
                                width="auto", 
                                className="d-flex justify-content-end mt-auto"
                            )
                        ),
                    ],
                    md=6,  # Form column width
                ),

                # Image Column with Card
                dbc.Col(
                    dbc.Card(
                        dbc.CardImg(
                            src="assets/HowtoPay.png",
                            top=True,
                            style={"width": "100%"}
                        ),
                        body=True,
                        style={
                            "width": "100%",  # Full width of the column
                            "padding": "10px",
                            "borderRadius": "10px",
                            "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.2)",  # Optional shadow for better emphasis
                            "marginTop": "15px"  # Align with form inputs
                        },
                    ),
                    md=4,  # Adjust width as needed for better alignment
                ),
            ],
            align="top",
            justify="start",
        ),
    ],
    className="p-4",  # Padding for the container
)
