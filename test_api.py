# test_api.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_valid_prediction():
    payload = {
        "engine_temp": 100.0,
        "altitude": 500.0,
        "vibration_level": 5.0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "failure_probability" in response.json()

def test_invalid_data_validation():
    # Test case: altitude out of range (max is 10000)
    payload = {
        "engine_temp": 100.0,
        "altitude": 99999.0, 
        "vibration_level": 5.0
    }
    response = client.post("/predict", json=payload)
    # 422 Unprocessable Entity is what FastAPI returns for validation errors
    assert response.status_code == 422

def test_extra_field_forbidden():
    # Test case: sending a field that isn't in our schema
    payload = {
        "engine_temp": 100.0,
        "altitude": 500.0,
        "vibration_level": 5.0,
        "malicious_code": "drop table users" 
    }
    response = client.post("/predict", json=payload)
    # Our Pydantic ConfigDict(extra='forbid') should trigger a 422
    assert response.status_code == 422