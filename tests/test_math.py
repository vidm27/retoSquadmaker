from mathematic import (
    calculate_least_common_multiple,
    convert_to_valid_number_list,
    determine_least_common_multiple,
)


def test_convert_to_valid_number_list():
    src_list = [
        {"list_test": [-5, -2, 0], "expected":[0]},
        {"list_test": [4,8,15,10,-13], "expected":[4,8,15,10,13]},
        {"list_test": [5, 2, 0], "expected":[5, 2]},
        {"list_test": [5, -2,0,-40,0], "expected":[5,2,40]},
    ]

    for number in src_list:
      result =convert_to_valid_number_list(number['list_test'])
      assert result == number['expected']

def test_mcm_is_correct():
    src_list = [
        {"list_test": [-5, -2, 0], "expected":0},
        {"list_test": [5, -2, 0], "expected":10},
        {"list_test": [2,5,6,8], "expected":120},
        {"list_test": [2,5,8,7,9], "expected":2520},
        {"list_test": [5, -2,0,-40,0], "expected":40},
    ]
    for numbers in src_list:
      result = determine_least_common_multiple(numbers['list_test'])
      assert result == numbers['expected']