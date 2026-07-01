# app/schemas.py
from pydantic import BaseModel, Field, ConfigDict

class SensorData(BaseModel):
    # Field constraints (ge=greater than or equal to, le=less than or equal to)
    # This prevents the model from receiving values it wasn't trained to handle.
    engine_temp: float = Field(..., ge=20, le=500, description="Temperature in Celsius")
    altitude: float = Field(..., ge=0, le=10000, description="Altitude in meters")
    vibration_level: float = Field(..., ge=0, le=10, description="Vibration index")

    # Hardening step: forbid any extra fields provided by a malicious/erroneous client
    model_config = ConfigDict(extra='forbid')

class PredictionResponse(BaseModel):
    status: str
    failure_probability: float
    model_version: str = "1.0.0"