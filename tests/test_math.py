from fastapi import HTTPException
from fastapi.testclient import TestClient

from main import app
from services.mathematic import (
    calculate_least_common_multiple,
    convert_to_valid_number_list,
    determine_least_common_multiple,
    multiply_numbers,
)

client = TestClient(app)


def test_convert_to_valid_number_list():
    src_list = [
        {"list_test": [0], "expected":[0]},
        {"list_test": [4, 8, 15, 10, -13], "expected":[4, 8, 15, 10, 13]},
        {"list_test": [5, 2, 0], "expected":[5, 2]},
        {"list_test": [5, -2, 0, -40, 0], "expected":[5, 2, 40]},
    ]

    for number in src_list:
        result = convert_to_valid_number_list(number['list_test'])
        assert result == number['expected']


def test_determine_correct_list_of_common_divisors():
    src_list = [
        {"list_test": [5, 8, 9], "expected":(2, 2, 2, 3, 3, 5)},
        {"list_test": [2,5,8,7], "expected":(2, 2, 2, 5, 7)},
    ]
    for numbers in src_list:
        result = determine_least_common_multiple(numbers['list_test'])
        assert result == numbers['expected']


def test_correct_multiply_list_number():
    src_list = [
        {"list_test": (2, 2, 2, 3, 3, 5), "expected": 360},
        {"list_test": (2, 2, 2, 5, 7), "expected": 280}
    ]
    for numbers in src_list:
        result = multiply_numbers(numbers['list_test'])
        assert result == numbers['expected']


def test_mcm_is_correct():
    src_list = [
        {"list_test": [5, 8, 9], "expected":360},
        {"list_test": [-5, -2, 0], "expected":0},
        {"list_test": [5, -2, 0], "expected":10},
        {"list_test": [2, 5, 6, 8], "expected":120},
        {"list_test": [2, 5, 8, 7, 9], "expected":2520},
        {"list_test": [4, -2, 0, -40, 0], "expected":40},
    ]
    for numbers in src_list:
        result = calculate_least_common_multiple(numbers['list_test'])
        assert result == numbers['expected']


def test_endpoint_return_correct_mcm():
    query_params = [{
        "endpoint": "/math/lcm/?numbers=55&numbers=-2&numbers=-3", "expected": 330,
        "endpoint": "/math/lcm/?numbers=-5&numbers=-2&numbers=-3", "expected": 0
    }]
    for query in query_params:
        endpoint:str = query['endpoint']
        response = client.get(endpoint)
        mcm_result = response.json()['result']
        assert mcm_result == query['expected']
