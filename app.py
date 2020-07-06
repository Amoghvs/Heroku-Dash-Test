#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 14:25:38 2020

@author: amogh
"""


 
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

ibu_values=[35, 60, 85, 75]
abv_values=[5.4, 7.1, 9.2, 4.3]
tabtitle='resume!'
myheading='Resume Survivor'
myheading2="Input a resume"



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    html.H2(myheading2)
   ]
)



if __name__ == '__main__':
    app.run_server()