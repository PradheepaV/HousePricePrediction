###s######################################################################################################
# Id            : V1.0 5 ML - house_price_predictor.py          
# Type          : Util
# Tests         : test_house_price_predictor.py
# Description   : Util to preprocess house price-area data and create machine learning model
#########################################################################################################

from scipy import stats
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression, ElasticNet
from sklearn.metrics import r2_score    
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR

import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import os
import pickle

SqFeet = [ 1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700 ]
Prices = [ 245000, 312000, 279000, 308000, 199000, 219000, 405000, 324000, 319000, 255000 ]

CV = 10
PARENT_DIR      = ""
MODEL_NAME      = "reg_model.pkl"

def read_data( data, columnNames, sep=";" ):
    ''' Reads file content and returns dataframe'''
    return pd.DataFrame(data, columns=columnNames)

def preprocess_data( df ): 
    ''' Process adata and drop the outliers (that are 3 sd away) '''
    z = np.abs( stats.zscore( df ) )
    df = df[ ( z < 3 ).all( axis=1 ) ]       
    plt.scatter( df[ 'SqFeet' ].ravel(), df[ 'Prices' ].ravel())
    plt.show()
    return df

def analyse_model( df ):
    '''Build various model and produce their performance statistics for analysis '''
    X = df[ 'SqFeet' ].ravel().reshape( -1, 1 )
    y = df[ 'Prices' ].ravel().reshape( -1, 1 )   
       
    models = [LinearRegression(),
              ElasticNet(),              
              RandomForestRegressor(n_estimators=2, max_features='sqrt'),
              KNeighborsRegressor(),
              SVR(kernel='linear'),              
              ]
 
    TestModels = pd.DataFrame()
    tmp = {}      
    for model in models:        
        m = str( model )        
        tmp[ 'Model' ] = m[ :m.index('(')] 
        model = GridSearchCV( model, param_grid={}, cv=CV )        
        model.fit( X, y )        
        y_pred = model.predict( X )
        tmp['R2_Price'] = r2_score(y, y_pred )
        TestModels = TestModels.append([tmp])
    
    TestModels.set_index('Model', inplace=True)
    _fig, axes = plt.subplots( ncols=1, figsize=(10, 4) )
    TestModels.R2_Price.plot( ax=axes, kind='bar', title='R2_Price' )
    print TestModels
    plt.show()
    
def build_model( df ):
    ''' Build the selected Model - LinearRegression'''
    rfr         = LinearRegression()
    X           = df[ 'SqFeet' ].ravel().reshape( -1, 1 )
    y           = df[ 'Prices' ].ravel().reshape( -1, 1 )
    reg_model   = GridSearchCV( rfr, param_grid={}, cv=CV )    
    reg_model.fit( X, y )     
    return reg_model

def persist_model( model, modelName="" ):
    ''' Pickle and dump the model locally '''
    model_file_path     = os.path.join( PARENT_DIR, modelName or MODEL_NAME )
    model_file_pickle   = open(model_file_path, 'wb')
    pickle.dump( model, model_file_pickle )
    model_file_pickle.close() 

if __name__ == '__main__':  
    df = read_data( zip( SqFeet, Prices ), ["SqFeet", "Prices"] )
    df = preprocess_data( df )   
    analyse_model( df ) 
    model = build_model( df )
    persist_model( model )
