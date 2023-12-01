file = open('inputD03.txt', 'r')
content = file.readlines()
file.close()

for line in range(len(content)):
    content[line] = content[line].strip('\n')


# 323 x 31

def toboggan(map, right, step=1):
    down_len = len(map)
    right_len = len(map[0])
    track = ''
    mov = right
    for steps in range(step, down_len, step):
        # print(steps)
        # print(mov)
        if mov >= right_len:
            mov = mov - right_len
            # print(f'NEW MOV: {mov}')
        track += map[steps][mov]
        mov += right
    print(track)
    print(len(track))
    trees = 0
    for item in track:
        if item == '#':
            trees += 1
    print(f' Trees : {trees}')
    return trees


first = toboggan(content, 1)
second = toboggan(content, 3)
third = toboggan(content, 5)
fourth = toboggan(content, 7)
fifth = toboggan(content, 1, 2)

answer = first * second * third * fourth * fifth
print(f'Answer is {answer}')
