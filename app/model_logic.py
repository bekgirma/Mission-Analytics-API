# app/model_logic.py
import joblib
import pandas as pd

# Load the model globally once when the module is imported
# In a real mission system, you'd add logging here
try:
    model = joblib.load('model.pkl')
except FileNotFoundError:
    raise RuntimeError("model.pkl not found. Ensure it is in the root directory.")

def get_prediction(data: dict):
    # Convert incoming dict to DataFrame as expected by the Random Forest
    input_df = pd.DataFrame([data])
    
    # Get probability of class 1 (failure)
    probability = model.predict_proba(input_df)[0][1]
    return float(probability)