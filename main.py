from fastapi import FastAPI, HTTPException
from typing import Union


recipes = {1: "noodles, tomato sauce", 2:"bread, butter"}

app = FastAPI()

@app.get("/ping")
async def root():
    return "pong"

@app.get("/recipes")
async def read_recipes():
    return recipes

@app.get("/recipes/{id}")
async def read_item(id: int):
    if id not in recipes:
        raise HTTPException(status_code=404, detail="Recipe ID not found")
    return recipes[id]