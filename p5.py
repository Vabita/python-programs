def power(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result


base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")
