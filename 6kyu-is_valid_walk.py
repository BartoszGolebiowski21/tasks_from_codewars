# https://www.codewars.com/kata/54da539698b8a2ad76000228


def is_valid_walk(walk):
    if len(walk) == 10:
        location = [0, 0]
        for i in walk:
            if i == 'n':
                location[1] += 1
            elif i == 's':
                location[1] -= 1
            elif i == 'w':
                location[0] -= 1
            elif i == 'e':
                location[0] += 1
        if location == [0, 0]:
            return True
        else:
            return False
    return False


print(is_valid_walk(['n','n','n','w','n','s','s','e','s','s','s']))
