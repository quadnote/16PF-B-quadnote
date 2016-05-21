def factorial(n):
    if 1>= n:
        return 1
    else:
        return n+factorial(n-1)

    print(factorial(5))


#5! 을 계산하는법 (5x4x3x2x1=?)


f=1
for n in range(1,5+1):
    f*=n