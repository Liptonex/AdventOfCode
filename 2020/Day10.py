from main import open_txt_by_line

contents = open_txt_by_line('inputD10_ex.txt')
numbers = []
for line in contents:
    numbers.append(int(line))


def joltage(adapters):
    max_joltage = 0
    num_1_jolt = 0
    num_2_jolt = 0
    num_3_jolts = 1
    current_jolts = 0
    adapters.sort()
    defoult = []

    # print(adapters)
    max_joltage = adapters[-1] + 3
    for adapter in adapters:
        if adapter == current_jolts + 1:
            num_1_jolt += 1
            current_jolts = adapter
            defoult.append(adapter)
        elif adapter == current_jolts + 2:
            num_2_jolt += 1
            current_jolts = adapter
            defoult.append(adapter)
        elif adapter == current_jolts + 3:
            num_3_jolts += 1
            current_jolts = adapter
            defoult.append(adapter)
        else:
            print(f'NO! Adapter: {adapter}, joltage: {current_jolts}')
            break
    return max_joltage, num_1_jolt, num_2_jolt, num_3_jolts, defoult


x = joltage(numbers)
answer = x[1] * x[3]
print(x)
print(f'Answer: {answer}')


def arrange_joltage(adapters, num_1_jolt, num_2_jolt, num_3_jolt, defoult):
    bank = set()
    for adapter in adapters:
        bank.add(adapter)
    i = 0
    options = [[]]
    current = 0
    searching = True

    return bank


print(arrange_joltage(numbers, x[1], x[2], x[3], x[4]))
