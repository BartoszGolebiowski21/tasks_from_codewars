# https://www.codewars.com/kata/5612ab201830eb000f0000c0


def no_of_divs(number):
    no_of_divs = 0
    i = 1
    while i*i <= number:
        if number % i == 0:
            if i*i == number:
                no_of_divs += 1
            else:
                no_of_divs += 2
        i += 1
    return no_of_divs

def find_min_num(num_div):
    number = 1
    while no_of_divs(number) != num_div:
        number += 1
        print(number, no_of_divs(number))
    return number

print(find_min_num(80))