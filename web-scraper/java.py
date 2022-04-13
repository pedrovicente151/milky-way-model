def dash_insert(numbers: int):

    new_num = str(numbers)
    new_str = ""

    for i in range(len(new_num) - 1):
        left = new_num[i]
        right = new_num[i + 1]

        int_left = int(left)
        int_right = int(right)


        # Evens
        if (int_left % 2 == 0 and int_right % 2 == 0):
            new_str += left
            new_str += "*"
            new_str += right
        #  Odds
        elif (int_left % 2 == 1 and int_right % 2 == 1):
            new_str += left
            new_str += '-'
            new_str += right



        #
        #
        #
        # #  None
        # else:
        #     if left not in new_str:
        #         new_str += left
        #
        #     if right not in new_str:
        #         new_str += right

        # else:
        #     new_str += right

    print(new_str)






if __name__ == '__main__':
    dash_insert(132634)