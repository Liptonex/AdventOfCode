with open('Inputs/Day_04.txt', 'r') as file:
    contents = file.readlines()

print(contents)
drawn_numbers = list(map(int, contents[0].split(',')))
print(drawn_numbers)

del contents[0:2]

all_boards = []
board = []
for line in contents:
    if line == '\n':
        all_boards.append(board)
        board = []
    else:
        board.append(list(map(int, line.rstrip('\n').split())))

del board
all_columns = []
columns = []
column = []

for board in all_boards:
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            column.append(board[j][i])
        columns.append(column)
        column = []
    all_columns.append(columns)
    columns = []
#
# for b in all_boards:
#     print(f'Board num: {all_boards.index(b)}')
#     for r in b:
#         print(r)
#     print('       ---       ')
#     for c in all_columns[all_boards.index(b)]:
#         print(c)
#     print('-----------------')

while drawn_numbers:
    x = drawn_numbers.pop(0)
    print(f'CURRENT NUMBER: {x}')
    for board in all_boards:
        print(f'Board num: {all_boards.index(board)}')
        for row in board:
            for number in row:
                if number == x:
                    row.remove(x)
            print(row)
            if not row:
                drawn_numbers = []
        if not drawn_numbers:
            break
    for board in all_columns:
        print('       ---       ')
        print(f'Board num: {all_columns.index(board)}')
        for column in board:
            for number in column:
                if number == x:
                    column.remove(x)
            print(column)
            if not column:
                drawn_numbers = []
        if not drawn_numbers:
            break
        print('---------------------')

wining = [[91, 22, 89, 72, 82], [63, 58, 80, 42, 45], [], [17, 62, 14, 35], [65, 79, 0]]
summ = 0
for l in wining:
    summ += sum(l)

print(summ * 90)
