def checkOdd(ch):
    return ((ord(ch) - 48) & 1)


def Insert_dash(num_str):
    result_str = num_str

    # Traverse the string character by character
    x = 0
    while (x < len(num_str) - 1):

        # Compare every consecutive
        # character with the odd value
        if (checkOdd(num_str[x]) and checkOdd(num_str[x + 1])):
            result_str = (result_str[:x + 1] + '-' + result_str[x + 1:])
            num_str = result_str
            x += 1
        x += 1

    # Print the resultant string
    return result_str


# Driver Code

# Given number in form of string
str = "1745389"

# Function call
print(Insert_dash(str))