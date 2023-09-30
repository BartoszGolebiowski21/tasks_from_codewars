# https://www.codewars.com/kata/5552101f47fc5178b1000050


def dig_pow(n, p):
    digits = [int(digit) for digit in str(n)]
    digits_2 = []
    for digit in digits:
        digit_2 = digit ** p
        p += 1
        digits_2.append(digit_2)
    if sum(digits_2) % n == 0:
        return sum(digits_2) / n
    return -1

print(dig_pow(89, 1))
print(dig_pow(46288, 3))
print(dig_pow(92, 1))