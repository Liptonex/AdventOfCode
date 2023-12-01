with open('Inputs/Day_02.txt', 'r') as file:
    content = file.readlines()

processed = []
for item in content:
    new_item = item.rstrip('\n').split()
    new_item[1] = int(new_item[1])
    processed.append(tuple(new_item))

print(processed)

horizontal = 0
depth = 0

for navigation in processed:
    if navigation[0] == 'forward':
        horizontal += navigation[1]
    elif navigation[0] == 'down':
        depth += navigation[1]
    elif navigation[0] == 'up':
        depth -= navigation[1]

print(f'Final position {horizontal*depth}')

print('--- Second part ---')

horizontal = 0
depth = 0
aim = 0

for navigation in processed:
    if navigation[0] == 'forward':
        horizontal += navigation[1]
        depth += navigation[1]*aim
    elif navigation[0] == 'down':
        aim += navigation[1]
    elif navigation[0] == 'up':
        aim -= navigation[1]

print(f'Final position {horizontal*depth}')