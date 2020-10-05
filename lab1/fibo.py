def fibonacci(n):
    a = 1
    b = 1
    c = 0
    count = 0
    while c < n :
        c = a + b
        a = b
        b = c
        count += 1 
    return b - a , a, b 
