from main import open_txt_by_line
import copy

contents = open_txt_by_line('inputD08.txt')
commands = []

for line in contents:
    commands.append(tuple(line.split()))

print(commands)


def acc(command, accumulator, i):
    if "+" in command:
        num = int(command.strip('+'))
        accumulator += num
        i += 1
    elif '-' in command:
        num = int(command.strip('-'))
        accumulator -= num
        i += 1
    return accumulator, i


def jmp(command, i):
    # print(f'JMP: {command}')
    if '+' in command:
        num = int(command.strip('+'))
        i += num
    elif '-' in command:
        num = int(command.strip('-'))
        i -= num
    return i


def t_machine(original):
    accumulator = 0
    commands_list = copy.deepcopy(original)
    commands_num = len(commands_list)
    print(f'Original {original}')
    i = 0
    n = 0
    j = 0
    posible_commands = set(range(i, commands_num))
    running = True
    checking = True
    nops = []
    jmps = []
    for number in range(0, commands_num):
        operation, value = commands_list[number]
        if operation == 'nop':
            nops.append(number)
        elif operation == 'jmp':
            jmps.append(number)
    while checking:
        while running:
            # print(f'I: {i}')
            # print(f'Set at the begining: {posible_commands}')
            operation, value = commands_list[i]
            # print(f'Op: {operation}')
            posible_commands.remove(i)
            if operation == 'nop':
                i += 1
            elif operation == 'acc':
                accumulator, i = acc(value, accumulator, i)
            elif operation == 'jmp':
                i = jmp(value, i)
            if i not in posible_commands:
                # print(f'What is possible: {posible_commands}, what I have: {i}')
                running = False
        # print(f'nops: {nops}')
        if i == commands_num:
            print("DONE!")
            checking = False
        else:
            if n < len(nops):
                # print(f' n: {n}')
                commands_list = copy.deepcopy(original)
                # print(commands_list)
                # print(f'Original {original}')
                operation, value = commands_list[nops[n]]
                commands_list[nops[n]] = 'jmp', value
                print(f'Changed line {nops[n]} to jmp')
                n += 1
                accumulator = 0
                i = 0
                posible_commands = set(range(i, commands_num))
                running = True
            elif j < len(jmps):
                commands_list = copy.deepcopy(original)
                # print(commands_list)
                # print(f'Original {original}')
                operation, value = commands_list[jmps[j]]
                commands_list[jmps[j]] = 'nop', value
                print(f'Changed line {jmps[j]} to nop')
                j += 1
                accumulator = 0
                i = 0
                posible_commands = set(range(i, commands_num))
                running = True
            else:
                print("OOOPS")
                break
    return accumulator, posible_commands, n, len(nops), j, len(jmps), i, commands_num


print(t_machine(commands))
