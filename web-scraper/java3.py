def dash_insert(numbers: int):
    num_str = str(numbers)

    i = 0

    while i < len(num_str) - 1:

        left = num_str[i]
        right = num_str[i+1]

        int_left = int(left)
        int_right = int(right)

        #  Checking Evens
        if (int_left % 2 == 0 and int_right % 2 == 0):
            num_str = num_str[:i + 1] + '*' + num_str[i + 1:]
            i += 1

        #  Checking Odds
        elif (int_left % 2 == 1 and int_right % 2 == 1):
            num_str = num_str[:i + 1] + '-' + num_str[i + 1:]
            i += 1

        i += 1



if __name__ == '__main__':
    dash_insert(0000)