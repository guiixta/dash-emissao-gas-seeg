#import pandas as pd;
import plotly as px
import dash
from dash import html, dcc


app = dash.Dash(__name__);


app.layout = html.Div(children=[
    html.H1('Page.py')
    
]);
