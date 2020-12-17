import pandas as pd

file = open('inputD02.txt', 'r')
content = file.readlines()
file.close()
data = [[], [], [], []]

for item in content:
    rule, password = item.split(':')
    data[3].append(password.strip('\n').strip(' '))
    nums, letter = rule.split()
    data[2].append(letter)
    begining_num, end_num = nums.split('-')
    data[0].append(int(begining_num))
    data[1].append(int(end_num))

diki = {'beg_num': data[0], 'end_num': data[1], 'letter': data[2], 'password': data[3]}

df = pd.DataFrame(diki)
# print(df.head())
quans = []

for row in range(len(df)):
    quan = 0
    for char in df['password'][row]:
        # print(char)
        if char == df['letter'][row]:
            quan += 1
    quans.append(quan)

df['quan'] = quans
# print(df)
validity = []
for row in range(len(df)):
    if df['quan'][row] < df['beg_num'][row]:
        validity.append(False)
    elif df['quan'][row] > df['end_num'][row]:
        validity.append(False)
    else:
        validity.append(True)
df['validity'] = validity
# print(df)

how_many = 0
for row in range(len(df)):
    if df['validity'][row] == True:
        how_many += 1

print(how_many)

new_validity = []
for row in range(len(df)):
    if df['password'][row][df['beg_num'][row] - 1] == df['letter'][row] and df['password'][row][df['end_num'][row] - 1] != df['letter'][row]:
        new_validity.append(True)
    elif df['password'][row][df['beg_num'][row] - 1] != df['letter'][row] and df['password'][row][df['end_num'][row] - 1] == df['letter'][row]:
        new_validity.append(True)
    else:
        new_validity.append(False)

df['new_valid'] = new_validity
# print(df)

how_many_new = 0
for row in range(len(df)):
    if df['new_valid'][row] == True:
        print(df['password'][row], df['beg_num'][row], df['end_num'][row], df['letter'][row])
        how_many_new += 1

print(how_many_new)
