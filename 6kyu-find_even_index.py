# https://www.codewars.com/kata/5679aa472b8f57fb8c000047


def find_even_index(arr):
    i = 0
    while i < len(arr):
        if sum(arr[0:i]) == sum(arr[i+1:len(arr)]):
            return i
        else:
            i += 1
    return -1



print(find_even_index([20,10,30,10,10,15,35]))
print(find_even_index([1,2,3,4,3,2,1]))


