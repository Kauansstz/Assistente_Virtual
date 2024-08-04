def rec(n):
    if n < 2:
        print(rec(n - 1))


print(rec(0))
