def squares(n=10):
    results = []
    for i in range(n+1):
        yield i**99



for x in squares(10):
    print(x)