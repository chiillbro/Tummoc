from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import math

app = FastAPI()

class Coordinates(BaseModel):
    latitude1: float
    longitude1: float
    latitude2: float
    longitude2: float

@app.post("/calculate-distance/")
def calculate_distance(coords: Coordinates):
    try:
        # Extract coordinates from the request body
        x1, y1 = coords.latitude1, coords.longitude1
        x2, y2 = coords.latitude2, coords.longitude2

        # Calculate the distance using the distance formula
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        return {"distance": distance}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error calculating distance: {str(e)}")

# A simple test endpoint to check if the server is running
@app.get("/")
def read_root():
    return {"message": "Hello World"}
