# https://adventofcode.com/2020/day/1/input

file = open('inputD01.txt', 'r')
content = file.readlines()
file.close()
numbers = []
for item in content:
    item.strip('\n')
    numbers.append(int(item))
del content
# print(numbers)

for x in numbers:
    for y in numbers:
        if x + y == 2020:
            print(f' For two: {x * y}')
        for z in numbers:
            if x + y + z == 2020:
                print(f'For three: {z * y * x}')
