from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():

    return {"Server":"Running"}

@app.post("/analyze")
def analyze():

    print("Incident Detected!")

    return {"Status":"Success"}