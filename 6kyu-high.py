# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272


def high(string):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_dict = {letter: alphabet.index(letter) + 1 for letter in alphabet}
    word_dict = {}
    for word in string.split():
        word_points = 0
        for letter in word:
            if letter in alphabet:
                print(letter, alphabet_dict[letter])
                word_points += alphabet_dict[letter]
            word_dict[word] = word_points
        print("sum of word:", word, word_points)
        print("-")

    return max(word_dict, key=word_dict.get)

print(high('man i need a taxi up to ubud'))