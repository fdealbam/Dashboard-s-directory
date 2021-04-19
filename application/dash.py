import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import numpy as np
import dash_table
import sidetable as stb
import datetime
from datetime import datetime, timedelta
from datetime import date
import geopandas as gpd
import flask
import os
yesterday = datetime.now() - timedelta(1)
yea = datetime.strftime(yesterday, '%Y%m%d')

today = date.today()
d2 = today.strftime("Fecha de actualización : %d-%m-%Y")







##



app = dash.Dash(external_stylesheets=[dbc.themes.SKETCHY])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H6("Dashboards´s Collection", className="display-6"),
        html.Hr(),
        html.P(
            "", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("COVID-19", href="https://camaradiputados.herokuapp.com/", active="exact"),
                dbc.NavLink("Feminicidios", href="https://feminicidios.herokuapp.com/", active="exact"),
                dbc.NavLink("Violencia familiar", href="https://violenciafamiliar.herokuapp.com/", active="exact"),
                dbc.NavLink("Violación", href="https://violacion.herokuapp.com/", active="exact"),
                dbc.NavLink("Abuso sexual", href="https://abusosexual.herokuapp.com/", active="exact"),
                dbc.NavLink("Vacunas SRE", href="https://vacunassre.herokuapp.com/", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P(d2)
    elif pathname == "/page-1":
        return html.P(d2),
    
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
   # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
from application.dash import app
from settings import config

if __name__ == "__main__":
    app.run_server()
