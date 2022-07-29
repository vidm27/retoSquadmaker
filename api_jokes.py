import requests

api_jokes = {
    "chuck":
        {
            "api": "https://api.chucknorris.io/jokes/random",
            "key_joke": "value"
        },
    "dad": {
        "api": "https://icanhazdadjoke.com/",
        "key_joke": "joke"
    }
}


def select_joke(select_api) -> str:
    try:
        api = api_jokes[select_api]
        respose = requests.get(
            api['api'],
            headers={
                "accept": "application/json"
            }
        )
        key_joke = api['key_joke']
        result = respose.json()
        return result[key_joke]
    except KeyError:
        raise
