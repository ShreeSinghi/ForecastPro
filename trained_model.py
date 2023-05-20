from flask import Flask, jsonify, render_template
from ts_models import multivariate_ts_lstm
import pandas as pd
import numpy as np
import sklearn
import json
import pickle

data = pd.read_csv('data/portfolio_data.csv')[['AMZN', 'NFLX', 'DPZ']]
data = sklearn.preprocessing.MinMaxScaler().fit_transform(data)
data = np.array(data)

model = multivariate_ts_lstm(n_past_days=21, batch_size=32)
test, predictions = model.train_predict(data)
    
test_json = json.dumps(test.tolist())
predictions_json = json.dumps(predictions.tolist())

# Convert test and predictions to JSON format
test_json = json.dumps(test.tolist())
predictions_json = json.dumps(predictions.tolist())

# Write the JSON data to separate files
with open('test.json', 'w') as test_file:
    test_file.write(test_json)

with open('predictions.json', 'w') as predictions_file:
    predictions_file.write(predictions_json)

# return 'JSON files generated successfully.'