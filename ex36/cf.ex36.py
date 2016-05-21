# if에 반드시 else를 넣어라
# if문의 깊이를 깊게하지마라
# 하나의 독립된 문단처럼 앞뒤 공간을 주라
# 논리식을 최대한 간단히 하라
# 무한루프를 최대한 자제하고 for 문으로 풀어서 써라



import sys

def factorial(n):
    if 1 == n:
        return 1
    elif 1 < n:
        return n * factorial(n-1)
    else
        print("impossible! n = %d" %n)
        sys.exit(0)

        print(factorial(-1))

