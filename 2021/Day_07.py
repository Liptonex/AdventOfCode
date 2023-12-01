import numpy as np
import math

with open('Inputs/Day_07.txt', 'r') as f:
    content = f.readlines()

crabs_start = []
for i in content:
    crabs_start = list(map(int, i.split(',')))

# crabs_start = np.array(crabs_start)
# answers = np.array([])
# print(f'Options 0 -- {np.amax(crabs_start)}')
# for i in range(0, np.amax(crabs_start)):
#     if i % 5 == 0:
#         print(f'Checking {i}')
#     pos = np.repeat(i, len(crabs_start))
#     distance = np.abs(np.subtract(crabs_start, pos))
#     answers = np.append(answers, np.sum(distance))
#
# print(f'Final answers: {answers}')
# x = np.amin(answers)
# print(f'Minimal amunt of fuel: {x}')
# print(f'Position: {np.where(answers == x)[0]}')

### Part two ###

crabs_start = np.array(crabs_start)
answers = np.array([])
fuel_list = []
print(f'Options 0 -- {np.amax(crabs_start)}')
for i in range(0, np.amax(crabs_start)):
    # print(f'Checking {i}')
    if i % 5 == 0:
        print(f'Checking {i}')
    pos = np.repeat(i, len(crabs_start))
    distance = np.abs(np.subtract(crabs_start, pos))
    fuel_list = []
    for item in distance:
        fuel = np.sum(np.arange(item + 1))
        fuel_list.append(fuel)
    answers = np.append(answers, np.sum(np.array(fuel_list)))

print(f'Final answers: {answers}')
x = np.amin(answers)
print(f'Minimal amunt of fuel: {x}')
print(f'Position: {np.where(answers == x)[0]}')
