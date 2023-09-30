# https://www.codewars.com/kata/52efefcbcdf57161d4000091


# def count(s):
#     dict = {}
#     for char in s:
#         dict[char] = s.count(char)
#     return dict
    
def count(s):
    return {char: s.count(char) for char in s}


# from collections import Counter
# def count(string):
#     return Counter(string)

print(count("aba"))