from main import open_txt_by_line

data = open_txt_by_line('inputD04.txt')
# print(len(data))
passports = [[]]
current = 0
for item in data:
    if item == '':
        passports.append([])
        current += 1
    else:
        passports[current].append(item)

for passport in range(len(passports)):
    entries = ''
    for entry in range(len(passports[passport])):
        entries += ' ' + passports[passport][entry]
    # print(entries)
    passports[passport] = entries

for document in range(len(passports)):
    passports[document] = passports[document].split()
    for item in range(len(passports[document])):
        passports[document][item] = passports[document][item].split(':')


# print(passports[0])


def automatic_passport_scanner(pasport):
    length = len(pasport)
    essential_data = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    optional_data = {'cid'}
    for item_num in range(length):
        if pasport[item_num][0] in essential_data:
            if pasport[item_num][0] == 'byr':
                year = pasport[item_num][1]
                if len(year) == 4:
                    if 1920 <= int(year) <= 2002:
                        essential_data.remove(pasport[item_num][0])
            elif pasport[item_num][0] == 'iyr':
                year = pasport[item_num][1]
                if len(year) == 4:
                    if 2010 <= int(year) <= 2020:
                        essential_data.remove(pasport[item_num][0])
            elif pasport[item_num][0] == 'eyr':
                year = pasport[item_num][1]
                if len(year) == 4:
                    if 2020 <= int(year) <= 2030:
                        essential_data.remove(pasport[item_num][0])
            elif pasport[item_num][0] == 'hgt':
                number = pasport[item_num][1].strip('cm').strip('in')
                unit = pasport[item_num][1][-2:]
                if unit == 'cm':
                    if 150 <= int(number) <= 193:
                        essential_data.remove(pasport[item_num][0])
                elif unit == 'in':
                    if 59 <= int(number) <= 76:
                        essential_data.remove(pasport[item_num][0])
            elif pasport[item_num][0] == 'hcl':
                color = pasport[item_num][1]
                if color[0] == '#':
                    color = list(color.strip('#'))
                    q = 0
                    if len(color) == 6:
                        for sign in color:
                            if sign.isdigit() or sign.isalpha() and sign.islower():
                                q += 1
                        if q == 6:
                            essential_data.remove(pasport[item_num][0])
            elif pasport[item_num][0] == 'ecl':
                color = pasport[item_num][1]
                eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
                if color in eye_colors:
                    essential_data.remove(pasport[item_num][0])
            elif pasport[item_num][0] == 'pid':
                number = pasport[item_num][1]
                if len(number) == 9:
                    q = 0
                    for sign in number:
                        if sign.isdigit():
                            q += 1
                    if q == 9:
                        essential_data.remove(pasport[item_num][0])
    if essential_data == set():
        return True
    else:
        return False


valid = []
how_many = 0
for document in passports:
    valid.append(automatic_passport_scanner(document))
for i in valid:
    if i:
        how_many += 1

print(f'{how_many} passports are valid')
