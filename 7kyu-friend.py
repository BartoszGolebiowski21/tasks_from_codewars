# https://www.codewars.com/kata/55b42574ff091733d900002f


def friend(x):
    list_of_friends = []
    for element in x:
        if len(element) == 4:
            list_of_friends.append(element)
        else:
            continue
    return list_of_friends


print(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]))