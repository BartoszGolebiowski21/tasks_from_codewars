# https://www.codewars.com/kata/546f922b54af40e1e90001da


def alphabet_position(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = []
    for i in list(text.lower()):
        if i in alphabet:
            result.append(str(alphabet.index(i) + 1))
    return ' '.join(result)


print(alphabet_position("The sunset sets at twelve o' clock."))