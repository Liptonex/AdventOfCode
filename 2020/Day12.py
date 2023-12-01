from main import open_txt_by_line

contents = open_txt_by_line('inputD12.txt')


def manchattan_distace(instructions):
    # facing = 'E'
    compass = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
    waypoint = {'N': 1, 'E': 10, 'S': 0, 'W': 0}
    wind_rose = ['N', 'E', 'S', 'W']

    instructions = [[item[0], int(item[1:])] for item in instructions]
    for navi in instructions:
        print(f'Compass: {compass}; Waypoint: {waypoint}; Next move: {navi}')
        if navi[0] == 'F':
            times = navi[1]
            for i in range(0, times):
                compass['N'] = compass['N'] + waypoint['N']
                compass['E'] = compass['E'] + waypoint['E']
                compass['S'] = compass['S'] + waypoint['S']
                compass['W'] = compass['W'] + waypoint['W']
        elif navi[0] == 'N':
            waypoint['N'] += navi[1]
        elif navi[0] == 'S':
            waypoint['S'] += navi[1]
        elif navi[0] == 'E':
            waypoint['E'] += navi[1]
        elif navi[0] == 'W':
            waypoint['W'] += navi[1]
        elif navi[0] == 'L':
            # print(f'Old facing {facing}')
            position = 0
            change = int(navi[1] / 90)
            new_position = position - change
            if new_position < 0:
                new_position = new_position + 4
            # print(position, new_position)
            # print(waypoint)
            indexes = []
            for i in range(len(wind_rose)):
                j = i + new_position
                if j >= len(wind_rose):
                    j = j - len(wind_rose)
                indexes.append(j)
            new_waypoint = {wind_rose[indexes[0]]: waypoint[wind_rose[0]],
                            wind_rose[indexes[1]]: waypoint[wind_rose[1]],
                            wind_rose[indexes[2]]: waypoint[wind_rose[2]],
                            wind_rose[indexes[3]]: waypoint[wind_rose[3]]}
            waypoint = new_waypoint.copy()
        elif navi[0] == 'R':
            # print(f'Old facing {facing}')
            position = 0
            change = int(navi[1] / 90)
            new_position = position + change
            if new_position >= len(wind_rose):
                new_position = new_position - 4
            # print(position, new_position)
            # print(waypoint)
            indexes = []
            for i in range(len(wind_rose)):
                j = i + new_position
                if j >= len(wind_rose):
                    j = j - len(wind_rose)
                indexes.append(j)
            new_waypoint = {wind_rose[indexes[0]]: waypoint[wind_rose[0]],
                            wind_rose[indexes[1]]: waypoint[wind_rose[1]],
                            wind_rose[indexes[2]]: waypoint[wind_rose[2]],
                            wind_rose[indexes[3]]: waypoint[wind_rose[3]]}
            # print(new_waypoint)
            waypoint = new_waypoint.copy()
            # facing = wind_rose[new_position]
            # print(f'Change {navi}')
            # print(f'New facing: {facing}')
    distance = abs(compass['E'] - compass['W']) + abs(compass['N'] - compass['S'])
    return compass, distance


print(manchattan_distace(contents))
