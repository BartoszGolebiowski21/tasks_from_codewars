# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132


def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        list_of_true_or_false = []
        for character in pin:
            try:
                int(character)
                list_of_true_or_false.append(True)
            except ValueError:
                list_of_true_or_false.append(False)
        return all(list_of_true_or_false)
    return False


print(validate_pin("1234"))
print(validate_pin("12345"))
print(validate_pin("a123"))