from typing import Union
import uvicorn
import os
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
 
)

@app.get("/")
def home():
    return "hello from root"

@app.get("/api")
def read_root():

    message = "Success from /api. Hello from Python container!"
    return message

@app.get("/api/profile")
def read_root():
    message = "Hello from /api/profile on port 5000 from a different private subnet!"
    return message

if __name__ == '__main__':
    # uvicorn.run(app, host="backend", port=5000)
    uvicorn.run(app, host="0.0.0.0", port=5000)