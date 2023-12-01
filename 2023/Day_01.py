# Part 1 #

print('### Test part ###')
with open('Data/01_test.txt', 'r') as file:
    content = file.readlines()
content.append('\n')

print('Raw file content:')
print(content)

lines = [line.rstrip('\n') for line in content]

print('Pre-processed file content:')
print(lines)

num = []
for line in lines:
    num_chars = ''
    for char in line:
        if char.isdigit():
            num_chars += char
    if num_chars != '':
        first = num_chars[0]
        last = num_chars[-1]
        num.append(int(first + last))

print('Numbers to sum:')
print(num)

print('Final sum:')
print(sum(num))

print('### Actual data part ###')

with open('Data/01_data.txt', 'r') as file:
    content = file.readlines()
content.append('\n')
lines = [line.rstrip('\n') for line in content]
num = []
for line in lines:
    num_chars = ''
    for char in line:
        if char.isdigit():
            num_chars += char
    if num_chars != '':
        first = num_chars[0]
        last = num_chars[-1]
        num.append(int(first + last))
print('Final sum:')
print(sum(num))

# Part 2 #

print('###### Second star #######')
print('### Test part ###')
with open('Data/01_test_2.txt', 'r') as file:
    content = file.readlines()
content.append('\n')

print('Raw file content:')
print(content)

lines = [line.rstrip('\n') for line in content]

print('Pre-processed file content:')
print(lines)

NUMBERS = {
    'one' : 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'zero': 0
}

num = []
for line in lines:
    num_chars = ''
    alpha_chars = ''
    for char in line:
        if char.isdigit():
            num_chars += char
        else:
            alpha_chars += char
            for key in NUMBERS.keys():
                if key in alpha_chars:
                    num_chars += str(NUMBERS.get(key))
                    alpha_chars = ''
    if num_chars != '':
        print('All numbers in line:')
        print(num_chars)
        first = num_chars[0]
        last = num_chars[-1]
        num.append(int(first + last))

print('Numbers to sum:')
print(num)

print('Final sum:')
print(sum(num))

print('### DATA PART ###')

with open('Data/01_data.txt', 'r') as file:
    content = file.readlines()
content.append('\n')
lines = [line.rstrip('\n') for line in content]

num = []
for line in lines:
    num_chars = ''
    alpha_chars = ''
    for char in line:
        if char.isdigit():
            num_chars += char
        else:
            alpha_chars += char
            for key in NUMBERS.keys():
                if key in alpha_chars:
                    num_chars += str(NUMBERS.get(key))
                    alpha_chars = ''
    if num_chars != '':
        print('All numbers in line:')
        print(line)
        print(num_chars)
        first = num_chars[0]
        last = num_chars[-1]
        num.append(int(first + last))

print('Numbers to sum:')
print(num[-10:])

print('Final sum:')
print(sum(num))
