import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 1. Generate synthetic "Mission Sensor" data
def generate_data(n_samples=1000):
    np.random.seed(42)
    data = {
        'engine_temp': np.random.uniform(20, 500, n_samples),
        'altitude': np.random.uniform(0, 10000, n_samples),
        'vibration_level': np.random.uniform(0, 10, n_samples)
    }
    df = pd.DataFrame(data)
    # Define a failure condition: higher temp + higher vibration = likely failure
    df['failure'] = ((df['engine_temp'] > 400) | (df['vibration_level'] > 8)).astype(int)
    return df

# 2. Train and save the model
df = generate_data()
X = df.drop('failure', axis=1)
y = df['failure']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X_train, y_train)

# 3. Export as a persistent file for your API to use
joblib.dump(model, 'model.pkl')
print("Model trained and saved as model.pkl")