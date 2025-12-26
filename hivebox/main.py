from fastapi import FastAPI

SENSOR_1 = "652e8e6711af9800081e07a1"
SENSOR_2 = "6544e051439231000708a30f"
VERSION = "v0.0.1"
app = FastAPI()

@app.get("/", summary="Return the main API")
def read_root():
    return {"message": "Welcome to your FastAPI app!"}

@app.get("/version", summary="Return the current App Version")
def version():
    """
        Return the current App version 
    """
    return {"version":VERSION}
