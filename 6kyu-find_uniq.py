# https://www.codewars.com/kata/585d7d5adb20cf33cb000235


def find_uniq(arr):
    for i in list(set(arr)):
        if arr.count(i) == 1:
            return i


print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))