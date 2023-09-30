# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064


def row_sum_odd_numbers(n):
    starting_number = n ** 2 - n + 1
    ending_number = n ** 2 + n - 1
    odd_numbers_from_range = [element for element in range(starting_number, ending_number + 1) if element % 2 == 1]
    sum = 0
    for element in odd_numbers_from_range:
        sum += element
    return sum

# def row_sum_odd_numbers(n):
#     return n ** 3

print(row_sum_odd_numbers(5))
