from fastapi import FastAPI
from kafkasupport import produce
app = FastAPI()
app.include_router(produce.router)
@app.get('/home')
def home():
    return {"HomePAGE"}