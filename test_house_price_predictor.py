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
    preprocess_data, persist_model, analyse_model, build_model, persist_model
from mock import patch
import matplotlib.pyplot

class ProductClassifierTests(unittest.TestCase): 

    def setUp(self): 
        self.df = pd.DataFrame( (zip( SqFeet, Prices ) ), columns=["SqFeet", "Prices"] )
  
    @patch('matplotlib.pyplot.show')
    def test_preprocess_data( self, patch_plot ):         
        self.assertTrue( preprocess_data(self.df) is not None )
    
    def test_read_data( self ):    
        self.assertTrue( zip( SqFeet, Prices ), ["SqFeet", "Prices"] ) 
    
    def test_persist_model( self ):
        persist_model( self.df, modelName="Dummy" )#filename to be datetime stamped to be unique everytime
        self.assertTrue( os.path.isfile(os.path.join( PARENT_DIR, "Dummy" )) )
    
    @patch('matplotlib.pyplot.show')
    def test_analyse_model( self, patch_plot ):
        ''' Ensure it runs without any error'''
        analyse_model( self.df )
        
    def test_build_model( self ):
        '''Ensure it runs without any error'''
        build_model( self.df )

if __name__ == '__main__':    
    unittest.main()
