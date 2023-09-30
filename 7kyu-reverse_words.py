# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4


# def reverse_words(text):
#     return ' '.join([word[::-1] for word in text.split(' ')])


def reverse_words(text):
    reversed_string_list = []
    word_list = []
    for character in text:
        if character == " ":
            word_string = ''.join(word_list)
            reversed_string_list.append(word_string[::-1])
            word_list.clear()
            reversed_string_list.append(character)
        else:
            word_list.append(character)
    word_string = ''.join(word_list)
    reversed_string_list.append(word_string[::-1])
    return ''.join(reversed_string_list)


print(reverse_words("This is an example!"))
print(reverse_words("double  spaces"))