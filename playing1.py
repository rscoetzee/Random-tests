
import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn import svm
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
import pandas as pd


melbourne_data = pd.read_csv('melb_data.csv')

melbourne_data.describe()
melbourne_data = melbourne_data.dropna(axis=0)

y = melbourne_data.Price

melbourne_features = ['Rooms','Bathroom','Landsize','Lattitude','Longtitude']
X = melbourne_data[melbourne_features]

melbourne_model = DecisionTreeRegressor(random_state=1)

melbourne_model.fit(X,y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are:")

print(melbourne_model.predict(X.head()))

predicted_home_prices = melbourne_model.predict(X)
MAE = mean_absolute_error(y,predicted_home_prices)
print(MAE)

