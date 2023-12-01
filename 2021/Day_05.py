with open('Inputs/Day_05.txt', 'r') as file:
    contents = file.readlines()

processed = []
for line in contents:
    split_line = line.rstrip('\n').split('->')
    for position in split_line:
        x, y = tuple(position.split(','))
        processed.append((int(x), int(y)))

print(processed)
points = []

for i in range(1, len(processed), 2):
    start = processed[i - 1]
    print(f'Start: {start}')
    end = processed[i]
    print(f'End: {end}')
    if start[0] == end[0]:
        print('Pionowo')
        if end[1] > start[1]:
            for n in range(start[1], end[1] + 1):
                points.append((start[0], n))
        if start[1] > end[1]:
            for n in range(end[1], start[1] + 1):
                points.append((start[0], n))
    elif start[1] == end[1]:
        print('Poziomo')
        if end[0] > start[0]:
            for n in range(start[0], end[0] + 1):
                points.append((n, start[1]))
        if start[0] > end[0]:
            for n in range(end[0], start[0] + 1):
                points.append((n, start[1]))
    else:
        print('Krzywo')
        if start[0] < end[0]:
            if start[1] < end[1]:
                x = [n for n in range(start[0], end[0] + 1)]
                print(x)
                y = [m for m in range(start[1], end[1] + 1)]
                print(y)
                for i in range(len(x)):
                    points.append((x[i], y[i]))
            elif end[1] < start[1]:
                x = [n for n in range(start[0], end[0] + 1)]
                print(x)
                y = [m for m in range(start[1], end[1] - 1, -1)]
                print(y)
                for i in range(len(x)):
                    points.append((x[i], y[i]))
        elif end[0] < start[0]:
            if start[1] < end[1]:
                x = [n for n in range(start[0], end[0] - 1, -1)]
                y = [m for m in range(start[1], end[1] + 1)]
                for i in range(len(x)):
                    points.append((x[i], y[i]))
            elif end[1] < start[1]:
                x = [n for n in range(start[0], end[0] - 1, -1)]
                print(x)
                y = [m for m in range(start[1], end[1] - 1, -1)]
                print(y)
                for i in range(len(x)):
                    points.append((x[i], y[i]))

# print(points)

target = set()
n = 0
x = len(points)
for point in points:
    n += 1
    if n % 1000 == 0:
        print(f'{n} / {x}')
    if points.count(point) > 1:
        target.add(point)

print(f'Final answer: {len(target)}')
