def generate_combinations_recursive(prefix, length, alphabet, result):
    if length == 0:
        result.append(prefix)
        return
    for char in alphabet:
        generate_combinations_recursive(prefix + char, length - 1, alphabet, result)


def generate_combinations():
    alphabet = "ABC"
    result = []
    generate_combinations_recursive("", 1, alphabet, result)
    generate_combinations_recursive("", 2, alphabet, result)
    generate_combinations_recursive("", 3, alphabet, result)

    return result


combinations_list = generate_combinations()

for combination in combinations_list:
    print(combination)
