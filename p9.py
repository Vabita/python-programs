def convert_case(input_string):
    converted_string = ""
    for char in input_string:
        if char.isupper():
            converted_string += char.lower()
        else:
            converted_string += char.upper()
    return converted_string


input_string = input("Enter a string: ")
output_string = convert_case(input_string)
print("Converted string:", output_string)
