opening_brackets = ['(', '{', '<', '[']
closing_brackets = [')', '}', '>', ']']

while True:

    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    java_code = '\n'.join(lines)

    list = []

    for bracket in java_code:
        if bracket in opening_brackets:
            list.append(bracket)

        elif bracket in closing_brackets:
            position = closing_brackets.index(bracket)

            if (len(list) > 0) and (opening_brackets[position] == list[len(list) - 1]):
                list.pop()

    if len(list) == 0:
        print("\nBrackets are correctly nested.")
    else:
        print("\nBrackets are not correctly nested!")

    break