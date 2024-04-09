from fastapi import FastAPI

app = FastAPI(
    description = "this is simple app"
)

@app.get("/")

async def root():
    return {"mssg":"hello world"}