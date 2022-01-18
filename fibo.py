import time

def fiboRecursivo(n):
    time.sleep(0.1)

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fiboRecursivo(n-1) + fiboRecursivo(n-2)
