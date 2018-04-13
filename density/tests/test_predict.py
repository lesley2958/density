import pytest
import pandas as pd 

from density import predict 
from .predict import db_to_pandas, predict_tomorrow

def test_predict(app):
    resp = app.get('/predict')
    assert resp.status_code == 200

# test db_to_pandas
# only need to test if the dataframe correctly converts to pd
def test_db_to_pandas():
	data = db_to_pandas(g.cursor)

	# assert dataframe has correct number of rows (buildings)
	assert len(data.index) == 23

	# assert each row has correct number of columns
	for index, row in data.iterrows():
		assert len(row) == 6

# test predict_tomorrow
# need to test if the calculations for averages are correct
def test_predict_tomorrow():   
	data = db_to_pandas(g.cursor)         # loading data from current database connection
	predictions = predict_tomorrow(data)  # get predictions

	# assert dataframe is in correct format
	for index, row in predictions.iterrows():
		print(index, row)

	return 0;

test_predict_tomorrow()