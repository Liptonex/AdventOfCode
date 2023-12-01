with open('Inputs/Day_09.txt', 'r') as f:
    content = f.readlines()

map = []
for line in content:
    map.append([char for char in line.rstrip('\n')])

for line in map:
    print(line)


def lowpoints_finder(map):
    lowpoints = []
    height = len(map)
    width = len(map[0])
    for h in range(height):
        if h == 0:
            for w in range(width):
                if w == 0:
                    point = map[h][w]
                    right = map[h][w + 1]
                    bottom = map[h + 1][w]
                    if point < right and point < bottom:
                        lowpoints.append(int(point) + 1)
                elif w == width - 1:
                    point = map[h][w]
                    left = map[h][w - 1]
                    bottom = map[h + 1][w]
                    if point < left and point < bottom:
                        lowpoints.append(int(point) + 1)
                else:
                    point = map[h][w]
                    left = map[h][w - 1]
                    bottom = map[h + 1][w]
                    right = map[h][w + 1]
                    if point < left and point < bottom and point < right:
                        lowpoints.append(int(point) + 1)
        elif h == height - 1:
            for w in range(width):
                if w == 0:
                    point = map[h][w]
                    right = map[h][w + 1]
                    top = map[h - 1][w]
                    if point < right and point < top:
                        lowpoints.append(int(point) + 1)
                elif w == width - 1:
                    point = map[h][w]
                    left = map[h][w - 1]
                    top = map[h - 1][w]
                    if point < left and point < top:
                        lowpoints.append(int(point) + 1)
                else:
                    point = map[h][w]
                    left = map[h][w - 1]
                    top = map[h - 1][w]
                    right = map[h][w + 1]
                    if point < left and point < top and point < right:
                        lowpoints.append(int(point) + 1)
        else:
            for w in range(width):
                if w == 0:
                    point = map[h][w]
                    right = map[h][w + 1]
                    top = map[h - 1][w]
                    bottom = map[h + 1][w]
                    if point < right and point < top and point < bottom:
                        lowpoints.append(int(point) + 1)
                elif w == width - 1:
                    point = map[h][w]
                    left = map[h][w - 1]
                    top = map[h - 1][w]
                    bottom = map[h + 1][w]
                    if point < left and point < top and point < bottom:
                        lowpoints.append(int(point) + 1)
                else:
                    point = map[h][w]
                    left = map[h][w - 1]
                    top = map[h - 1][w]
                    right = map[h][w + 1]
                    bottom = map[h + 1][w]
                    if point < left and point < top and point < right and point < bottom:
                        lowpoints.append(int(point) + 1)
    return lowpoints


print(lowpoints_finder(map))
print(sum(lowpoints_finder(map)))
