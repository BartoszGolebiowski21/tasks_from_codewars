# https://www.codewars.com/kata/5592e3bd57b64d00f3000047


def find_nb(m):
    n = 1
    sum = 0
    while sum < m:
        sum += n ** 3
        if sum == m:
            return n
        n += 1
    return -1

print(find_nb(100))
print(find_nb(1071225))