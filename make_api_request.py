#########################################################################################################
# Id            : 4 ML - make_api_requests.py          
# Type          : Util
# Tests         : None
# Description   : Module to make API requests
#########################################################################################################

import requests
import pandas as pd

cacert = "certificate.pem" 

def make_api_request(data):
    # url for api
    url = 'https://localhost:3200/api'
    # make post request
    r = requests.post( url,pd.DataFrame(data).to_json(), verify=cacert )
    print r.text
    return r.text
    
inputData = { 'SqFeet': [100, 2000, 6578, 3000, 3564754985] }
make_api_request( inputData )
