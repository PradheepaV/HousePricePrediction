Procedure to run the model
======================
1. Add __init__.py to create module. The file could not be uploaded here as its an empty file.
2. Run house_price_predictor -
	This shows the performance of various models
	and persists Linear Regression model
3. Run house_price_predictor_api - 
	conda install -c anaconda cheroot (if not already available)
	This will bring up the server and run from port 5000
4. Use make_api_request -
	This will pass in various house areas(in sq feet), for which the house price is predicted and returned in the response.
