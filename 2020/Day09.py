from main import open_txt_by_line

contents = open_txt_by_line('inputD09.txt')
numbers = []

for line in contents:
    numbers.append(int(line))


# print(numbers)


def check_code(xmas, preambule=25):
    found = None
    for num in range(preambule, len(xmas)):
        possible_pairs = [xmas[i] + xmas[j] for i in range(num - preambule, len(xmas)) for j in
                          range(num - preambule + 1, len(xmas))]
        # print(possible_pairs)
        if xmas[num] in possible_pairs:
            print(f'{xmas[num]} is OK')
        elif xmas[num] not in possible_pairs:
            print(f'{xmas[num]} is missing')
            found = xmas[num]
            break
    return found


def find_contiguous(found_num, xmas):
    found_list = None
    searching = True
    running = True
    start = 0
    current = 1
    while searching:
        running_sum = xmas[start]
        running_list = [xmas[start]]
        while running:
            running_sum += xmas[current]
            print(f'SUM: {running_sum}')
            running_list.append(xmas[current])
            current += 1
            if running_sum == found_num:
                searching = False
                running = False
                found_list = running_list
            elif running_sum > found_num:
                running = False
        start += 1
        print(f'RESTART: {start}')
        current = start + 1
        running = True
        if start > len(xmas) or current > len(xmas):
            running = False
            searching = False
            print('I ran out of options!')
            # print(start, current, len(xmas))
    found_list.sort()
    answer = found_list[0] + found_list[-1]
    return answer


x = check_code(numbers)
print("_____________________________________")
print(find_contiguous(x, numbers))
