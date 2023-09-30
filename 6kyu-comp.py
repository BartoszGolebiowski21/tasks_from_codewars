# https://www.codewars.com/kata/550498447451fbbd7600041c


def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    if len(array1) != len(array2):
        return False
    list_of_truth = []
    for i in array1:
        if i**2 in array2:
            list_of_truth.append(True)
            array2.remove(i**2)
    return len(list_of_truth) == len(array1)


print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]))