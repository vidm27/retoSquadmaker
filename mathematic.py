from operator import mul
from typing import List

from sqlalchemy import true


def calculate_least_common_multiple(numbers: List) -> int:
    numbers = [5, 7, 9, 11, 15, 20]
    common_values = ()
    common_div = 2
    new_number = list(numbers)
    if len(new_number) == 1:
        print(f"Least Common Multiple Number: {new_number[0]}")
    else:
        while len(new_number) != 0:
            # print(f"Current list number: {new_number}")
            current_list = list(new_number)
            exist_common_div = 0
            index = 0
            current_line_div = False
            while index < len(current_list):
                number = current_list[index]

                result = number / common_div
                # print(
                #     f"**** result: {result}, common:{common_div}, number:{number}, index: {index}")
                if number % common_div == 0:
                    current_line_div = True
                    exist_common_div = + 1

                    if result == 1.0:
                        new_number.pop(index)
                        current_list = list(new_number)
                        continue

                    new_number[index] = int(result)

                index += 1

            if current_line_div:
                common_values += (common_div,)
                continue

            fix_len = len(current_list) - 1
            if exist_common_div == 0 or fix_len == 0:
                # print(f"Existing common divisor: {common_div}")
                common_div += 1

            print(common_values)

        res = 1
        for i in common_values:
            res = mul(i, res)

        print(f"Least common divisor: {res}")
        return res
