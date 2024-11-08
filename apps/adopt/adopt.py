import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

from app import app

# instead of app.layout, we just use the variable "layout" here
# We cannot really modify the "app" variable here, we only do it in index.py
layout = html.Div(
    [
        html.P("< Back"),
        html.H1("ADOPTION APPLICATION"),
        html.P("Hi Hooman! Thank you for your interest in giving a furever home to one of our rescues. We have a lot of rescue dogs and cats ready for adoption both at the BULACAN SHELTER and the BACOLOD SHELTER. Our adoption process is super easy!"),
        html.P("Adoption Process:"),
        html.Ol(
            [
                html.Li("Fill out this form and wait to be contacted by the team. Please give us at least 1 WEEK to do our initial screening."),
                html.Li("Go through an interview via Zoom or Facebook Messenger with one of our volunteers"),
                html.Li(" Visit the shelter, pay the Adoption Fee (P1000) and bring home your new best fur friend (once you pass the interview)")
            ]
        ),
        html.P("Undecided about adopting but you want to learn more about what it takes to be a fur parent? Go ahead and fill out this form and one of our volunteers will reach out to you to help assess if you're well-equipped to take on one of our rescues."),
        html.P("IMPORTANT: Our Shelters are located in BULACAN and BACOLOD. Adopters should be willing to travel to our Shelters to meet and pick-up the Rescue they want to adopt. "),
        html.P("Please also note that starting January 2022, we will already be implementing a PHP1,000 ADOPTION FEE to help with the upkeep of the shelter and also to cover what we have spent for the rescues’ rehabilitation. We also want to make sure that our adopters have the capacity to meet the needs of our rescues, who we all treat as family."),
        dbc.Button("Register", color='dark', href="/register", style={'margin': '0 10px'})
    ], style={"paddingTop":"200px","paddingLeft":"150px","paddingRight":"150px","paddingBottom":"200px","backgroundColor":"#FAF3EB"}
)
