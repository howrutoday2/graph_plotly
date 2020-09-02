from flask import Flask, render_template, request, redirect, Response
from flask_restful import Resource, Api
import requests

import numpy as np
import pandas as pd
# import plotly
# import plotly.graph_objs as go
# import plotly.utils.PlotlyJSONEncoder
import json


app = Flask(__name__,
            template_folder = "templates",
            static_folder = "static")
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods =['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')


@app.route("/graph_ploty", methods =['GET', 'POST'])
def plotly2():
    if request.method == 'GET':
        return render_template('plotly_3.html')
    elif request.method == 'POST':

        call_id = request.form['text']
        # 20200701083525010348629670009
        print("result form  ",call_id)
        result_load = "./static/result_0828_12.csv"
        # call_id = '20200701083525010348629670009'
        df_o = pd.read_csv(result_load, index_col = 0)
        df = df_o[df_o['call_id(t)']==call_id]
        df.to_json('./data/test.json', orient='table')
        file_path = "./data/test.json"
        with open(file_path, "r") as json_file:
            sample = json.load(json_file)

    # print(sample)
        return render_template('plotly_3.html', data = json.dumps(sample))   


if __name__ == "__main__":
    app.run(port = '8000')

