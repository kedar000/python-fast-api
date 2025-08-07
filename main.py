from fastapi import FastAPI
app = FastAPI()

@app.get('/')
async def root():
    return {"data" : {"name" : "Kedar" , "age " : 10}}

@app.get("/my-info")
async def info():
    return {"info" : {"Name" : "Kedar" , "Language" : "Python" }}
    