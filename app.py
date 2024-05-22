import pandas as pd
from flask import Flask
from flask import request
from flask import jsonify
from modules.insurance_model import InsuranceModel


app =Flask(__name__)

@app.route("/")
def index():
    return "API Prediction Model Service(BETA)"

@app.route("/predict",methods=['POST'])
def predict():
     data=request.get_json()
     df=pd.DataFrame(data, index=[0])
   
     result_predict= InsuranceModel().runModel(df, typed='single')
   
     return jsonify({
         "status":"predicted",
         "prdeic result":result_predict
     })

if __name__ =="__main__":
    app.run(port=5000)