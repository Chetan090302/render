from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class Input(BaseModel):
    name: str
    age: int

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

lis=[]

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.post("/post_data")
def post_data(data:Input):
    lis.append(data.model_dump())
    return {"message":"Data received successfully"}

@app.get("/get_data")
def get_data():
    return {"data":lis}
