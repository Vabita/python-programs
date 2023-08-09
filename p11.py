def count_words(input_string):
    words = input_string.split()
    return len(words)


input_string = input("Enter a string: ")
word_count = count_words(input_string)
print("Number of words:", word_count)
