def spam(divideBy):
    try:
        # Any code in this block that causes ZeroDivisionError won't crash the program
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: Invalid argument.")


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
