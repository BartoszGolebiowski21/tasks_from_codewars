# https://www.codewars.com/kata/5648b12ce68d9daa6b000099


def number(bus_stops):
    no_of_passengers = 0
    for element in bus_stops:
        no_of_passengers = no_of_passengers + element[0] - element[1]
    return no_of_passengers


# def number(bus_stops):
#     return sum(element[0] - element[1] for element in bus_stops)



bus_stops = [[10,0],[3,5],[5,8]]
print(number(bus_stops))