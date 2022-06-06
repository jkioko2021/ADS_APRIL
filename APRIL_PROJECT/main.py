# This is a sample Python script.
from dash import Dash ,html ,dcc
import plotly.graph_objects as pl
import pandas as pd
from dash.dependencies import  input, output
import requests
import json


app=Dash(__name__,suppress_callback_exceptions=True)
server=app.run_server
app.title="Africa  Data School"
app.description="This is a class Project for the ADS April 2022"


app.Layout=html.Div(children=[
    html.link(rel='shortcut icon',type='favicon.ico',href='assets.btc.png'),
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('btc.png'),id="ads-img",style={
                'height' : '60px',
                'width'  : 'auto',
                'margin-bottom' : '25px'
            })
        ],className='one-third column'),
        html.div([
            html.div([
                html.H1("Afica data School",style={'margin-bottom' : '0px','color' : 'pink', 'text-align' : 'center'}),
                html.H5("Afica data School", style={'margin-bottom': '0px', 'color': 'pink','text-align' : 'center'})
            ])
        ],className="one-third column",id='title')

    ],id='header',className='row flex-display', style={'margin-bottom' : '25px'}),
# -------------------Dropdown section-----------------------------#
html.Div([
    html.div([
        html.Label('Crypto Asset',style={'color' : '#FF00BD'}),
        dcc.Dropdown(
            id='coin',
            options=[
                {'label': 'Bitcoin', 'value': 'BTC'},
                {'label': 'Ethereum', 'value': 'ETH'},
                {'label': 'Bitcoin Cash', 'value': 'BCH'},
                {'label': 'Litecoin', 'value': 'LTC'}
            ],
            value='BTC'
        )
    ], className='card_container three columns'),


])
])

if __name__=="__main__":
    app.run_server(debug=True)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
