###s######################################################################################################
# Id            : V1.0 5 ML - test_house_price_predictor.py          
# Type          : Util
# Tests         : test_house_price_predictor.py
# Description   : Util to test house_price_predictor
#########################################################################################################

import pandas as pd
import pickle
import os

import unittest

from house_price_predictor import PARENT_DIR, MODEL_NAME, CV, SqFeet, Prices,\
    preprocess_data, persist_model

class ProductClassifierTests(unittest.TestCase): 

    def setUp(self): 
        self.df = pd.DataFrame( (zip( SqFeet, Prices ) ), columns=["SqFeet", "Prices"] )
  
    def test_preprocess_data(self):         
        self.assertTrue( preprocess_data(self.df) is not None )
    
    def test_read_data( self ):    
        self.assertTrue( zip( SqFeet, Prices ), ["SqFeet", "Prices"] ) 
    
    def test_persist_model( self ):
        persist_model( self.df, modelName="Dummy" )#filename to be datetime stamped to be unique everytime
        self.assertTrue( os.path.isfile(os.path.join( PARENT_DIR, "Dummy" )) )

if __name__ == '__main__':    
    unittest.main()