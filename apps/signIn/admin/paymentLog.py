import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

from app import app
from apps.sideNavbar import adminSideNavbar as aSN

layout=html.Div(
    [
        aSN.customerSidebar()
    ]
)
