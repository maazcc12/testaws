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


