from operator import mul
from typing import List, Tuple


def convert_to_valid_number_list(numbers:list):
    has_one_value_positive = False
    valid_numbers = []
    for number in numbers:
        if number > 0:
            has_one_value_positive = True
        positive = abs(number)
        valid_numbers.append(positive)
    
    if has_one_value_positive:
        return valid_numbers
    return [0]
    

def determine_least_common_multiple(numbers: List) -> int:
    """
        ALGORITHM: calculate the least common multiple
            2 - 5 - 8 -9 | 2
            1 - 5 - 4 -9 | 2
            1 - 5 - 2 -9 | 2
            1 - 5 - 1 -9 | 3
            1 - 5 - 1 -3 | 3
            1 - 5 - 1 -1 | 5
            1 - 1 - 1 -1 |
    """
    common_values = ()
    common_div = 2

    new_number = convert_to_valid_number_list(numbers)
    if len(new_number) == 1:
        return new_number[0]
    
    while len(new_number) != 0:
        # print(f"Current list number: {new_number}")
        current_list = list(new_number)
        exist_common_div = 0
        index = 0
        current_line_div = False
        while index < len(current_list):
            number = current_list[index]

            div_result = number / common_div
            # print(
            #     f"**** result: {result}, common:{common_div}, number:{number}, index: {index}")
            has_not_residue = (number % common_div) == 0
            if has_not_residue:
                current_line_div = True
                exist_common_div = + 1

                if div_result == 1.0:
                    new_number.pop(index)
                    current_list = list(new_number) # create new intances list 
                    continue

                new_number[index] = int(div_result)

            index += 1

        if current_line_div:
            common_values += (common_div,)
            continue

        fix_len = len(current_list) - 1
        if exist_common_div == 0 or fix_len == 0:
            # print(f"Existing common divisor: {common_div}")
            common_div += 1

        print(common_values)


    result = calculate_least_common_multiple(common_values)
    # print(f"Least common divisor: {result}")
    return result

def calculate_least_common_multiple(common_values: Tuple) -> int:
    res = 1
    for i in common_values:
        res = mul(i, res)
    return res