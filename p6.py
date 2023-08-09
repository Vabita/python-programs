def decimal_to_binary(decimal):
    return bin(decimal).replace("0b", "")


def decimal_to_octal(decimal):
    return oct(decimal).replace("0o", "")


def decimal_to_hexadecimal(decimal):
    return hex(decimal).replace("0x", "").upper()


def binary_to_decimal(binary):
    return int(binary, 2)


def octal_to_decimal(octal):
    return int(octal, 8)


def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)


decimal_num = int(input("Enter a decimal number: "))
binary_num = decimal_to_binary(decimal_num)
octal_num = decimal_to_octal(decimal_num)
hexadecimal_num = decimal_to_hexadecimal(decimal_num)

print("Decimal:", decimal_num)
print("Binary:", binary_num)
print("Octal:", octal_num)
print("Hexadecimal:", hexadecimal_num)

binary_input = input("Enter a binary number: ")
octal_input = input("Enter an octal number: ")
hexadecimal_input = input("Enter a hexadecimal number: ")

decimal_from_binary = binary_to_decimal(binary_input)
decimal_from_octal = octal_to_decimal(octal_input)
decimal_from_hexadecimal = hexadecimal_to_decimal(hexadecimal_input)

print("Binary to Decimal:", decimal_from_binary)
print("Octal to Decimal:", decimal_from_octal)
print("Hexadecimal to Decimal:", decimal_from_hexadecimal)
