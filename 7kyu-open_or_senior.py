# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa


# def open_or_senior(data):
#     for element in range(len(data)):
#         if data[element][0] >= 55 and data[element][1] > 7:
#             data[element] = "Senior"
#         else:
#             data[element] = "Open"
#     return data


def open_or_senior(data):
    categories = []
    for element in data:
        if element[0] >= 55 and element[1] > 7:
            categories.append("Senior")
        else:
            categories.append("Open")
    return categories


print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))