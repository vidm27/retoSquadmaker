from random import randint
from typing import List, Union

from databases import Database
from fastapi import FastAPI, HTTPException, Query, status

from schema.schema import Joke, JokeDB
from services.api_jokes import api_jokes, select_joke
from services.mathematic import calculate_least_common_multiple

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

@app.post('/jokes/')
async def save_joke(new_joke: Joke):
    try:
        query = "INSERT INTO jokes(value) VALUES(:value)"
        value = new_joke.dict()
        res = await database.execute(query=query, values=value)
        joke = JokeDB(**value, id=res)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Cann't save the new joke.")
    else:
        return joke


@app.put('/jokes/{joke_id}')
async def update_joke(joke_id: int, new_joke: Joke):
    try:
        query = "UPDATE jokes SET value = :joke_value WHERE id = :joke_id"
        value = {"joke_id": joke_id, "joke_value": new_joke.value}
        res = await database.execute(query=query, values=value)
        if int(res) == 0:
            raise Exception("joke not updated")
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Not update joke value for id: {joke_id}")


@app.delete('/jokes/{joke_id}')
async def delete_joke(joke_id: int):
    try:
        query = "DELETE FROM jokes WHERE id = :joke_id"
        value = {"joke_id": joke_id}
        res = await database.execute(query=query, values=value)
        if int(res) == 0:
            raise Exception("joke not delete")
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Not update joke value for id: {joke_id}")
    else:
        status.HTTP_202_ACCEPTED

@app.get('/math/lcm/')
async def get_least_common_multiple(numbers: Union[List[int], None] = Query(default=None)):
    try:
        mcm = calculate_least_common_multiple(numbers)
    except Exception as e:
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
