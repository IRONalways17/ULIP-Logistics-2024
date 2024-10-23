import pandas as pd
from sklearn.linear_model import LinearRegression

# Example dataset of delivery routes
data = pd.read_csv('routes_data.csv')

# Training a simple linear regression model for route time prediction
X = data[['distance', 'traffic_conditions', 'weather']]
y = data['delivery_time']

model = LinearRegression().fit(X, y)

# Prediction for a new route
new_route = [[10, 2, 1]]  # distance in km, traffic, weather conditions
predicted_time = model.predict(new_route)

print(f"Predicted delivery time: {predicted_time} minutes")
