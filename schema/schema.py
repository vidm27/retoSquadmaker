from pydantic import BaseModel, validator


class Joke(BaseModel):
    value: str

    @validator('value')
    def value_must_contain_empty_string(cls, value:str):
      sanatize_value = value.strip(' ')
      if '' == sanatize_value:
        raise ValueError('value joke muest contain empty string')
      return sanatize_value


class JokeDB(Joke):
    id: int
