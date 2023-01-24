from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get("/")
async def hello():
    return "Hello World!"


@app.get("/hello/{name}")
async def hello(name: str):
    return f"welcome {name}"


class AvailableCuisines(str, Enum):
    korean = "korean"
    japanese = "japanese"
    american = "american"
    italian = "italian"


food_items = {
    'korean': ['kimchi', 'bibimbap'],
    'japanese': ['sushi', 'ramen'],
    'american': ['hamburger', 'pizza'],
    'italian': ['pasta', 'pizza']
}

valid_cuisines = food_items.keys()


@app.get("/get_food/{cuisine}")
async def get_food(cuisine: str):

    if cuisine not in valid_cuisines:
        return f"{cuisine} is not valid cuisine."
    else:
        return food_items.get(cuisine)
