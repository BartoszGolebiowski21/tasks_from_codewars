# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029


def wave(people):
    result = []
    for i in range(len(people)):
        if people[i].isalpha() == True:
            people_2 = people[:i] + people[i].upper() + people[i+1:]
            result.append(people_2)
    return result



print(wave("hello"))
