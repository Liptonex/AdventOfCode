from main import open_txt_by_line

contetns = open_txt_by_line('inputD11_ex.txt')

seats = []

for line in contetns:
    seats.append(list(line))


def try_get(seat_list, row_num, seat_num):
    try:
        x = seat_list[row_num][seat_num]
        return x
    except IndexError:
        pass


def seats_chaos(seats_list):
    end_list = []
    for row in range(0, len(seats_list)):
        for seat in range(0, len(seats_list[row])):
            # print(f'Seat: {seats_list[row][seat]}')
            if seats_list[row][seat] == '.':
                end_list.append('.')
            elif seats_list[row][seat] == '#':
                if row == 0:
                    if seat == 0:
                        adjacent = [try_get(seats_list, row, seat + 1), try_get(seats_list, row + 1, seat),
                                    try_get(seats_list, row + 1, seat + 1)]
                    elif seat == 10:
                        adjacent = [try_get(seats_list, row, seat - 1), try_get(seats_list, row + 1, seat - 1),
                                    try_get(seats_list, row + 1, seat)]
                    else:
                        adjacent = [try_get(seats_list, row, seat - 1), try_get(seats_list, row, seat + 1),
                                    try_get(seats_list, row + 1, seat - 1), try_get(seats_list, row + 1, seat),
                                    try_get(seats_list, row + 1, seat + 1)]
                elif row == len(seats_list):
                    if seat == 0:
                        adjacent = [try_get(seats_list, row, seat + 1), try_get(seats_list, row - 1, seat),
                                    try_get(seats_list, row - 1, seat + 1)]
                    elif seat == 10:
                        adjacent = [try_get(seats_list, row, seat - 1), try_get(seats_list, row - 1, seat - 1),
                                    try_get(seats_list, row - 1, seat)]
                    else:
                        adjacent = [try_get(seats_list, row, seat - 1), try_get(seats_list, row, seat + 1),
                                    try_get(seats_list, row - 1, seat - 1), try_get(seats_list, row - 1, seat),
                                    try_get(seats_list, row - 1, seat + 1)]
                else:
                    if seat == 0:
                        adjacent = [try_get(seats_list, row, seat + 1),
                                    try_get(seats_list, row + 1, seat),
                                    try_get(seats_list, row + 1, seat + 1),
                                    try_get(seats_list, row - 1, seat),
                                    try_get(seats_list, row - 1, seat + 1)]
                    elif seat == 10:
                        adjacent = [try_get(seats_list, row, seat - 1),
                                    try_get(seats_list, row + 1, seat),
                                    try_get(seats_list, row + 1, seat - 1),
                                    try_get(seats_list, row - 1, seat),
                                    try_get(seats_list, row - 1, seat - 1)]
                    else:
                        adjacent = [try_get(seats_list, row, seat - 1), try_get(seats_list, row, seat + 1),
                                    try_get(seats_list, row + 1, seat - 1), try_get(seats_list, row + 1, seat),
                                    try_get(seats_list, row + 1, seat + 1), try_get(seats_list, row - 1, seat - 1),
                                    try_get(seats_list, row - 1, seat), try_get(seats_list, row - 1, seat + 1)]

                occupied = 0
                for ad_seat in adjacent:
                    if ad_seat == '#':
                        occupied += 1
                if occupied >= 4:
                    end_list.append('L')
                else:
                    end_list.append('#')
            elif seats_list[row][seat] == 'L':
                adjacent = [try_get(seats_list, row, seat - 1), try_get(seats_list, row, seat + 1),
                            try_get(seats_list, row + 1, seat - 1), try_get(seats_list, row + 1, seat),
                            try_get(seats_list, row + 1, seat + 1), try_get(seats_list, row - 1, seat - 1),
                            try_get(seats_list, row - 1, seat), try_get(seats_list, row - 1, seat + 1)]
                free = True
                for ad_seat in adjacent:
                    if ad_seat == "#":
                        free = False
                        # print("Here!")
                if free:
                    end_list.append('#')
                else:
                    end_list.append('L')
                    # print('####')
    # print(f' Seats: {seats_list}')
    # print(f'End: {end_list}')
    # print(f'Adjacent: {adjacent}')
    end_list = [end_list[i:i + 10] for i in range(0, len(end_list), 10)]
    print('DONE!')
    return seats_list, end_list


def stability_detector(seat_list):
    running = True
    x = seats_chaos(seat_list)
    while running:
        x = seats_chaos(x[1])
        if x[0] == x[1]:
            running = False
    return x

count = 0
stab = stability_detector(seats)
for row in stab[1]:
    print(''.join(row))
    for seat in row:
        if seat == '#':
            count += 1
print(count)

# Apparently I don't understand what they mean by 'adjacent'
