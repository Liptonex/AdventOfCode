def open_txt_by_line(filename):
    file = open(filename, 'r')
    content = file.readlines()
    file.close()

    for line in range(len(content)):
        content[line] = content[line].strip('\n')
    return content
