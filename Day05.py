from main import open_txt_by_line

content = open_txt_by_line('inputD05.txt')


# print(content)

def binary_seat_id(binary_code):
    row = 0
    column = 0
    rows_beg = 0
    rows_end = 128
    columns_beg = 0
    columns_end = 8
    row_code = list(binary_code[:7])
    column_code = list(binary_code[-3:])
    # print(row_code, column_code)
    for letter in row_code:
        q = round((rows_beg + rows_end) / 2, 0)
        if letter == "F":
            rows_end = q - 1
        elif letter == "B":
            rows_beg = q
        # print(letter)
        # print(f'Q: {q} -- rows: {rows_beg, rows_end}')
    if row_code[-1] == 'F':
        row = int(rows_beg)
    elif row_code[-1] == 'B':
        row = int(rows_end)
    for letter in column_code:
        q = round((columns_beg + columns_end) / 2, 0)
        if letter == "L":
            columns_end = q - 1
        elif letter == "R":
            columns_beg = q
        # print(letter)
        # print(f'Q: {q} -- columns: {columns_beg, columns_end}')
    if column_code[-1] == 'L':
        column = int(columns_beg)
    elif column_code[-1] == 'R':
        column = int(columns_end)
    seat_id = row * 8 + column
    return row, column, seat_id


boarding = set()

for item in content:
    boarding.add(binary_seat_id(item))

# print(boarding)

min_seat_id = 84
max_seat_id = 866
lacking = []
identical = []
ids = [i[2] for i in boarding]
ids.sort()
exclude = []
# print(ids)
for i in range(len(ids) - 1):
    if ids[i] + 1 != ids[i + 1]:
        if ids[i] == ids[i + 1]:
            identical.append(ids[i])
        else:
            # print(ids[i], ids[i + 1])
            lacking.append(ids[i])
print(lacking)
print(identical)
for id in lacking:
    for num in identical:
        if id + 2 == num:
            exclude.append((id, num))

for item in exclude:
    lacking.remove(item[0])
    identical.remove(item[1])
print(lacking)
print(identical)