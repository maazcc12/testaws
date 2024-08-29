from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

@app.post('/')
async def greet():
    return {"output":"Hello"}


@app.post('/bye')
async def intro():
    return {"output":"bye"}


@app.post('/test')
async def test():
    return {"output": "test"}


@app.post('/test_hello')
async def test_a():
    return {"output":"abc"}
