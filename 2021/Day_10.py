with open('Inputs/Day_10.txt', 'r') as f:
    content = f.readlines()

formatted = []
for line in content:
    formatted.append(line.rstrip('\n'))


def illegals(line):
    check = []
    opening = {'(', '[', '<', '{'}
    closing = {')', ']', '>', '}'}
    normal = {'(', ')'}
    square = {'[', ']'}
    pointy = {'<', '>'}
    curly = {'{', '}'}
    for char in line:
        if char in opening:
            # print(f'Opening: {char}')
            check.append(char)
        elif char in closing:
            # print(f'Closing {char}')
            last = check.pop()
            if {char, last} == normal:
                # print(f'Closed: {char} - {last}')
                continue
            elif {char, last} == square:
                # print(f'Closed: {char} - {last}')
                continue
            elif {char, last} == pointy:
                # print(f'Closed: {char} - {last}')
                continue
            elif {char, last} == curly:
                # print(f'Closed: {char} - {last}')
                continue
            else:
                # print(f'Not last: {char} ~ {last}')
                return False, char, [], None
    return True, None, check, line


# for x, y in enumerate(formatted):
#     print(x, y)

map = []

for n in range(0, len(formatted)):
    map.append(illegals(formatted[n]))

for x, y in enumerate(map):
    print(x, y)


def points_calc(map):
    score = 0
    normal = 3
    square = 57
    curly = 1197
    pointy = 25137
    for Boolean, sign, _, _ in map:
        if not Boolean:
            if sign == ')':
                score += normal
            elif sign == ']':
                score += square
            elif sign == '}':
                score += curly
            elif sign == '>':
                score += pointy
    return score


print(points_calc(map))


def discard_n_repair(evaluation):
    new_lines = []
    scores = []
    for Boolean, _, opened_list, original_line in evaluation:
        if Boolean:
            score = 0
            opened_list.reverse()
            for sign in opened_list:
                if sign == '(':
                    score *= 5
                    original_line += ')'
                    score += 1
                elif sign == '[':
                    score *= 5
                    original_line += ']'
                    score += 2
                elif sign == '{':
                    score *= 5
                    original_line += '}'
                    score += 3
                elif sign == '<':
                    score *= 5
                    original_line += '>'
                    score += 4
            new_lines.append(original_line)
            scores.append(score)
    return new_lines, scores


_, points = discard_n_repair(map)
points.sort()

middle = int(len(points)/2)
print(points[middle])