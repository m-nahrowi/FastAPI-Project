from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def reat_root():
    return {"Hello":"World"}