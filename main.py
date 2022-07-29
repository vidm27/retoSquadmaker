from random import randint
from typing import List, Union
from wsgiref.simple_server import demo_app

import requests
from databases import Database
from fastapi import FastAPI, HTTPException, Query, status

# from database import create_connection, disconnect, execute
from api_jokes import api_jokes, select_joke
from mathematic import calculate_least_common_multiple
from scheme import Joke, JokeDB

app = FastAPI()
database = Database('sqlite+aiosqlite:///jokes.db')


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/jokes/')
async def random_joke():
    type_api = list(api_jokes.keys())
    real_len = len(type_api) - 1
    random_select = randint(0, real_len)
    select_api = type_api[random_select]
    joke = select_joke(select_api)
    return joke


@app.get('/jokes/{type_joke}')
async def generate_joke(type_joke: str):
    try:
        print(f"Type joke value: {type_joke}")
        type_joke = type_joke.lower()
        joke = select_joke(type_joke)
    except KeyError as not_has_joke:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="This type of joke is not supported")
    else:
        return joke


@app.get('/math/lcm/')
async def get_least_common_multiple(numbers: Union[List[int], None] = Query(default=None)):
    try:
        mcm = calculate_least_common_multiple(numbers)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Invalid number: {numbers}")
    return {"result": mcm}


@app.get('/math/add/')
async def add_one_to_number(number: Union[str, int]):
    try:
        cast_number = int(number)
        operation_add = cast_number + 1
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The number passed was not a number: {number}")
    else:
        return {"result": operation_add}
