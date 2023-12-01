with open('Inputs/Day_01.txt', 'r') as file:
    content = file.readlines()

processed = []

for item in content:
    new_item = int(item.rstrip('\n'))
    processed.append(new_item)

answer = 0
x = processed[0]

for y in processed[1:]:
    if x < y:
        answer += 1
    x = y

print(answer)

answer = 0
# test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

for i in range(0, len(processed) - 3):
    A = sum(processed[i:i + 3])
    B = sum(processed[i + 1:i + 4])
    if A < B:
        answer += 1

print(answer)
