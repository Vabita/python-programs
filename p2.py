def fibonacci(n, a=0, b=1):
    if n <= 0:
        return
    else:
        print(a, end=", ")
        fibonacci(n - 1, b, a + b)


n = int(input("Enter the number of terms: "))
fibonacci(n)
