# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1


from collections import Counter

def duplicate_count(text):
    result = 0
    repetitions = Counter(text.lower())
    for element in repetitions.items():
        if element[1] > 1:
            result += 1
    return result


# def duplicate_count(text):
#     return len([letter for letter in set(text.lower()) if text.lower().count(letter) > 1])


print(duplicate_count("mErcedes"))
