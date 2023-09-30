# https://www.codewars.com/kata/52fba66badcd10859f00097e


def disemvowel(string_):
    vowels = "aeiouAEIOU"
    new_string = ""
    for character in string_:
        if character not in vowels:
            new_string += character
    string_ = new_string
    return new_string


print(disemvowel("This website is for losers LOL!"))