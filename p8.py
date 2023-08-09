def custom_length(input_string):
    length = 0
    for _ in input_string:
        length += 1
    return length


input_string = input("Enter a string: ")
length = custom_length(input_string)
print("Length of the string:", length)
