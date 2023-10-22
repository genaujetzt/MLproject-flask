from flask import Flask, render_template, request
import numpy as np
import sklearn
import xgboost
import pickle
app = Flask(__name__)
loaded_model = pickle.load(open('TreeRegressor.pickle', "rb"))
loaded_scaler = pickle.load(open("my_scaler.pickle", "rb"))
@app.route('/', methods = ["GET", "POST"])
def predict():
    message = ""
    if request.method == "POST":
        IW = request.form.get('IW')
        IF = request.form.get('IF')
        VW = request.form.get('VW')
        FP = request.form.get('FP')
        data = [[float(IW), float(IF), float(VW), float(FP)]]
        data = loaded_scaler.transform(data)
        pred = loaded_model.predict(data)
        print(pred)
        message = f"Width will be around {pred[0][0]} and Depth will be around {pred[0][1]}"
    return render_template('index.html', message = message)
app.run()