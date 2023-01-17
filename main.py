from fastapi import FastAPI

app = FastAPI()
app.title = "Tournament API"
app.version = "0.0.1"

@app.get("/", tags=["home"])
async def home():
    return {"message":"Home"}