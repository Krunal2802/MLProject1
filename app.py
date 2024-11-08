import pickle
import pandas as pd
import numpy as np
from Flask import Flask,request,render_template
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)

app = application

# route for home page
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictData',methods = ['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData()