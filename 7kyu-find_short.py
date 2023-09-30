# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9


def find_short(string):
    word_list = string.split()
    length_list = [len(word) for word in word_list]
    length_list.sort()
    return length_list[0]


print(find_short("bitcoin take over the world maybe who knows perhaps"))