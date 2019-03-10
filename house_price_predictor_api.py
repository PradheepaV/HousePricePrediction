#########################################################################################################
# Id            : V1.0 5 ML - house_price_predictor_api.py          
# Type          : Util
# Tests         : None
# Description   : Util to preprocess house price-area data and create machine learning model
#########################################################################################################

from flask import Flask, request
import pandas as pd
import numpy as np
import json
import pickle
import os

from house_price_predictor import PARENT_DIR, MODEL_NAME

app = Flask(__name__)

# Load Model Files
model_filepath = os.path.join( PARENT_DIR, MODEL_NAME )
model = pickle.load( open( model_filepath ) )

@app.route( '/api', methods=[ 'POST' ])
def make_prediction():
    ''' Make prediction based on the input text'''
    # read json object and conver to json string
    data = json.dumps( request.get_json(force=True) )
    # create pandas dataframe using json string
    df = pd.read_json( data )        
    X = df[ 'SqFeet' ].ravel().reshape( -1, 1 )
    # make predictions
    predictions = model.predict( X )    
    # create response dataframe
    df_response = pd.DataFrame( {'SqFeet': df[ 'SqFeet' ].ravel(), 'PredictedHousePrice' : predictions.ravel() } )
    return df_response.to_json()

@app.route( '/ping', methods=[ 'GET' ])
def test_ping():
    ''' test server https://localhost:3200/api '''
    return "alive"

if __name__ == '__main__':
    # host flask app at port 5200
    app.run(host = '127.0.0.1', port = 5200, ssl_context=('certificate.pem', 'key.pem'))

