with open('Inputs/Day_08.txt', 'r') as f:
    contents = f.readlines()

patterns = []
outputs = []

for line in contents:
    pattern, output = tuple(line.split('|'))
    patterns.append(pattern.rstrip('\n').split())
    outputs.append(output.rstrip('\n').split())

del pattern, output
print(outputs[0])


def get_codes(pattern_line):
    zero = 0  # -- 6
    one = 0  #
    two = 0  # -- 5
    three = 0  # -- 5
    four = 0  #
    five = 0  # -- 5
    six = 0  # -- 6
    seven = 0  #
    eight = 0  #
    nine = 0  # -- 6
    longer = []
    shorter = []

    for digit in pattern_line:
        if len(digit) == 3:
            seven = {char for char in digit}
            # print(f'7: {seven}')
        elif len(digit) == 2:
            one = {char for char in digit}
            # print(f'1: {one}')
        elif len(digit) == 4:
            four = {char for char in digit}
        elif len(digit) == 7:
            eight = {char for char in digit}
        elif len(digit) == 5:
            shorter.append({char for char in digit})
        elif len(digit) == 6:
            longer.append({char for char in digit})
    # print(shorter)
    # print(longer)
    # print(four)
    for d in longer:
        if four.issubset(d):
            nine = d
            longer.remove(d)
    for d in longer:
        if one.issubset(d):
            zero = d
        else:
            six = d
    for d in shorter:
        if one.issubset(d):
            three = d
            shorter.remove(d)
    for d in shorter:
        if d.issubset(six):
            five = d
        else:
            two = d
    codes = [zero, one, two, three, four, five, six, seven, eight, nine]
    return codes


decoded = []
number = []

for i in range(len(patterns)):
    number = []
    decoded.append([])
    code = get_codes(patterns[i])
    # print(code)
    for item in outputs[i]:
        number.append({char for char in item})
    for item in number:
        decoded[i].append(code.index(item))

print(decoded)
final_sum = 0

for list in decoded:
    text = ''
    for n in list:
        text += str(n)
    final_sum += int(text)

print(final_sum)
