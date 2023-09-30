# https://www.codewars.com/kata/556deca17c58da83c00002db


def tribonacci(signature, n):
    if n > 3:
        result = signature.copy()
        while n > 3:
            next_num = sum(signature)
            signature[0] = signature[1]
            signature[1] = signature[2]
            signature[2] = next_num
            result.append(next_num)
            n -= 1
        return result
    else:
        return signature[0:n]


print(tribonacci([3, 2, 1], 10))


