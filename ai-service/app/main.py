from fastapi import FastAPI

app = FastAPI(title="PharmaIQ AI Service")

@app.get("/")
def read_root():
    return {"message": "PharmaIQ AI Service is running"}