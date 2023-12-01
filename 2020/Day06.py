from main import open_txt_by_line

content = open_txt_by_line('inputD06.txt')
# print(content)
control_set = set()
# print(type(control_set))
answers = []

for i in range(len(content)):
    if content[i] == '':
        answers.append(len(control_set))
        # print(control_set)
        control_set = set()
    else:
        for letter in content[i]:
            control_set.add(letter)
answers.append(len(control_set))
# print(answers)
sum = 0
for number in answers:
    sum += number

print(f'Part one answer: {sum}')

# Second part
content.append("")
letters = set()
control_set = set()
group = []
final = []
for i in range(len(content)):
    if content[i] == '':
        print(group)
        for letter in control_set:
            present = set()
            for answer in group:
                if letter in answer:
                    present.add(True)
                elif letter not in answer:
                    present.add(False)
            if False in present:
                continue
            else:
                letters.add(letter)
        final.append(len(letters))
        print(letters)
        letters = set()
        control_set = set()
        group = []
    else:
        group.append(sorted(content[i]))
        for letter in content[i]:
            control_set.add(letter)

print(final)
sum = 0
for number in final:
    sum += number
print(f'Part two answer: {sum}')