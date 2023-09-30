# https://www.codewars.com/kata/576757b1df89ecf5bd00073b


def tower_builder(num_floors):
    tower = []
    for i in range(num_floors):
        num_spaces = num_floors - i - 1
        num_stars = 2 * i + 1
        floor = [' '] * num_spaces + ['*'] * num_stars + [' '] * num_spaces
        tower.append(''.join(floor))
    return tower

print(tower_builder(5))



# def tower_builder(n):
#     tower = []
#     for i in range(1, n + 1):
#         k = 2 * i - 1
#         string = ""
#         for p in range(1, k + 1):
#             string = string + "*"
#         tower.append(string)
#     return tower


# def tower_builder(number_of_floors):
#     elements_per_floor = 2 * number_of_floors - 1
#     floor = [' ' for p in range(1, elements_per_floor + 1)]
#     tower = [floor for i in range(1, number_of_floors + 1) ]
#     for i, floor in enumerate(tower):
#         num_spaces = number_of_floors - i - 1
#         num_stars = 2 * i + 1
#         floor[num_spaces:num_spaces+num_stars] = ['*' for _ in range(num_stars)]
    
#     return tower



# list = ['*','*','*','*','*','*','*','*','*']
# list[3] = ' '
# print(''.join(list))



# [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
#  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
#  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
#  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
#  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
