# The Lanternfish Symulator #
import numpy as np

with open('Inputs/Day_06_test.txt', 'r') as f:
    line = f.readlines()

fishy = list(map(int, line[0].split(',')))
print(fishy)

# def fish_factor(fishes, days=1):
#     young_fishy = []
#     for day in range(0, days):
#         # print(f'Day: {day}: fishes: {fishes}')
#         print(f'Day {day}')
#         young_fishy = []
#         for fish in range(len(fishes)):
#             if fishes[fish] == 0:
#                 young_fishy.append(8)
#                 fishes.pop(fish)
#                 fishes.insert(fish, 6)
#             else:
#                 birthday = fishes[fish]
#                 fishes.pop(fish)
#                 fishes.insert(fish, birthday - 1)
#         fishes += young_fishy
#     # print(f'Day: {days}: fishes: {fishes}')
#     return fishes


# target = fish_factor(fishy, 80)
# print(target)
# print(len(target))

### numpy version ###

fishy = np.array(fishy)


def fish_factor(fishes, days=1):
    for day in range(1, days+1):
        if day % 10 == 0:
            print(f'Day {day}')
        fishes = fishes - 1
        for fish in fishes:
            if fish == -1:
                fishes = np.append(fishes, 8)
        fishes = np.where(fishes == -1, 6, fishes)
        # print(f'Day: {day}: fishes: {fishes}')
    return fishes


target = fish_factor(fishy, 256)
print(target)
print(len(target))
