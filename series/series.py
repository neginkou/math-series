
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def lucas(n):
   
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        a, b = 2, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def sum_series(n, a=0, b=1):
    
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
