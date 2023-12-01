with open('Inputs/Day_03.txt', 'r') as file:
    content = file.readlines()

processed = []
for item in content:
    new_item = item.rstrip('\n')
    processed.append(new_item)

n = len(processed[0])
lines = []
for _ in range(0, n):
    lines.append([])


def most_frequent(some_list, top='1'):
    zeros = 0
    ones = 0
    for x in some_list:
        if x == '0':
            zeros += 1
        elif x == '1':
            ones += 1
        else:
            print('DA FUQ?', x)
    if zeros > ones:
        return '0'
    elif ones > zeros:
        return '1'
    elif ones == zeros:
        return top


def least_frequent(some_list, top='0'):
    zeros = 0
    ones = 0
    for x in some_list:
        if x == '0':
            zeros += 1
        elif x == '1':
            ones += 1
        else:
            print('DA FUQ?', x)
    if zeros > ones:
        return '1'
    elif ones > zeros:
        return '0'
    elif ones == zeros:
        return top


for item in processed:
    for i in range(0, n):
        lines[i].append(item[i])

gamma_binary = ''
epsilon_binary = ''

for place in lines:
    gamma_binary += most_frequent(place)
    epsilon_binary += least_frequent(place)

gamma = int(gamma_binary, 2)
epsilon = int(epsilon_binary, 2)

print(gamma * epsilon)

# --- second part ---

most = ''
least = ''

for i in range(0, n):
    print(f'Miejsce: {i}')
    lines = []
    for _ in range(0, n):
        lines.append([])
    for item in processed:
        for j in range(0, n):
            lines[j].append(item[j])
    print(f'kolumna teraz: {lines[i]}')
    most = most_frequent(lines[i])
    print(f'Najczęstrza: {most}')
    # least = least_frequent(lines[i])
    for _ in range(0, len(processed)):
        x = processed.pop(0)
        if x[i] == most:
            processed.append(x)
    print(processed)

oxygen = processed[0]
oxygen_int = int(oxygen, 2)
print(oxygen_int)

processed = []
for item in content:
    new_item = item.rstrip('\n')
    processed.append(new_item)

for i in range(0, n):
    print(f'Miejsce: {i}')
    lines = []
    for _ in range(0, n):
        lines.append([])
    for item in processed:
        for j in range(0, n):
            lines[j].append(item[j])
    print(f'kolumna teraz: {lines[i]}')
    # most = most_frequent(lines[i])
    # print(f'Najczęstrza: {most}')
    least = least_frequent(lines[i])
    print(f'Najrzadsza: {least}')
    for _ in range(0, len(processed)):
        x = processed.pop(0)
        if x[i] == least:
            processed.append(x)
    print(processed)
    if len(processed) == 1:
        break

co_2 = processed[0]
co_2_int = int(co_2, 2)
print(co_2_int)

print(oxygen_int * co_2_int)
