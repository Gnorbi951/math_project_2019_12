import random


def open_file():
    with open('szamsor.txt', 'r') as f:
        for line in f:
            if len(line) > 2:
                last_line = line
    return last_line


def get_input():
    with open('szamsor.txt', 'r') as f:
        for line in f:
            pass
        return line


def input_list_creator(comparer_line):
    input_list = []
    for letter in comparer_line:
        if letter != ' ':
            input_list.append(letter)
    input_list.remove('\n')
    return input_list


def append_to_file(text):
    number = random.randint(1, 2)
    with open('szamsor.txt', 'a') as f:
        f.write(text + '\n' + str(number))


def main():
    compare_line = open_file()
    compare_list = input_list_creator(compare_line)
    user_input = get_input()
    counter = 0
    output = [user_input]
    for number in compare_list:
        if str(number) == output[counter]:
            output.append('1')
        else:
            output.append('2')
        counter += 1

    output.pop(0)
    output = ' '.join(output)
    output = ' ' + output
    append_to_file(output)


if __name__ == '__main__':
    main()
