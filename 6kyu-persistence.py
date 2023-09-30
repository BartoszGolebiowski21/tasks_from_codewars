# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec


def persistence(n):
    no_of_iterations = 0
    while True:
        list_n = [int(i) for i in str(n)]
        if len(list_n) > 1:
            no_of_iterations += 1
            print(f"start of iteration {no_of_iterations}")
            print(list_n)
            result = 1
            for i in list_n:
                result = result * i
            n = result
        if len(list_n) == 1:
            return no_of_iterations

print(persistence(999))