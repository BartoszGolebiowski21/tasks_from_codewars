# https://www.codewars.com/kata/554ca54ffa7d91b236000023


def delete_nth(order,max_e):
    result = []
    for i in order:
        if result.count(i) < max_e:
            result.append(i)
    return result



print(delete_nth([20,37,20,21], 1))
print(delete_nth([1,1,3,3,7,2,2,2,2], 3))