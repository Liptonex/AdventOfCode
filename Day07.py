from main import open_txt_by_line

contents = open_txt_by_line('inputD07_ex2.txt')
rules = []

for line in contents:
    rules.append(line.split(' contain '))

for bags in rules:
    bags[0] = bags[0].split()
    if bags[1] == 'no other bags.':
        bags[1] = False
    elif ',' in bags[1]:
        bags[1] = bags[1].split(', ')
        for bag in range(len(bags[1])):
            bags[1][bag] = bags[1][bag].split()
    else:
        bags[1] = [bags[1].split()]
    # print(bags)

adj = 'shiny'
color = 'gold'


def search(fist_word, second_word):
    final_list = []
    global rules
    for rule in rules:
        if not rule[1]:
            continue
        else:
            for bag in rule[1]:
                # print(bag)
                if bag[1] == fist_word and bag[2] == second_word:
                    final_list.append(rule)
    return final_list


def full_search(first_word, second_word):
    bag_set = set()
    searching = True
    options = search(first_word, second_word)
    while searching:
        for hit in options:
            new = search(hit[0][0], hit[0][1])
            if not new:
                searching = False
            else:
                options += new
    for hit in options:
        bag = " ".join(hit[0])
        bag_set.add(bag)
    return bag_set


def inside_search(fist_word, second_word):
    final_list = []
    global rules
    for rule in rules:
        # print(rule)
        if not rule[1]:
            continue
        else:
            if rule[0][0] == fist_word and rule[0][1] == second_word:
                final_list.append(rule)
    # print(final_list)
    return final_list


def full_inside_search(first_word, second_word):
    bag_set = set()
    searching = True
    options = inside_search(first_word, second_word)
    print(options)
    i = 0
    while searching:
        # print(f'{i}| {options}')
        i += 1
        for hit in options:
            new = inside_search(hit[1][0][1], hit[1][0][2])
            if not new:
                searching = False
            else:
                print(new)
                options += new
    for hit in options:
        bag = " ".join(hit[0])
        # rule = " ".join(hit[1][0])
        # bag = bag + ' ' + rule
        bag_set.add(bag)
    return bag_set


#
# options = search(adj, color)
# print(options)
# # for hit in options:
# #     print(hit)
# print(len(options))

in_options = full_inside_search(adj, color)
# in_op = inside_search(adj, color)
# for hit in in_op:
#     print(hit[1][0][2])
print(in_options)
