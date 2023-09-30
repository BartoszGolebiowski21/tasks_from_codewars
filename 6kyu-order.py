# https://www.codewars.com/kata/55c45be3b2079eccff00010f


def order(sentence):
    dict = {}
    for word in sentence.split():
        for character in word:
            if character.isdigit():
                dict[word] = character
    sorted_keys = [key for key, value in sorted(dict.items(), key=lambda item: item[1])]
    return ' '.join(sorted_keys)

print(order("is2 Thi1s T4est 3a"))