from fastapi import FastAPI

app = FastAPI()

@app.post("/analyze")
def analyze():

    print("Alert received!")

    return {
        "status": "Analysis Started"
    }