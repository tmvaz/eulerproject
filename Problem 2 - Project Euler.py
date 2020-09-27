# PROJECT EULER - PROBLEM 2 (SOLUTION PROPOSAL)

# this version for the fibonacci function uses a rudimentary form of "memoizing"
# it calculates a number for the fibonacci series - and if that number was already
# calculated, it doesn't calculate it again
series = [0, 1]
def fibo(n):
    if n > 0:
        if n<=2:
            return series[n-1]
        elif n < len(series):
            return series[n-1]
        else:
            series.append(fibo(n-1) + fibo(n-2))
            return series[-1]

print(fibom(3), memo)
""" not finished yet
i = 0
res = 0
while(True):
    z = fibonacci(i)
    if z%2 == 0:
        res = res + z
    elif z > 4000000:
        break
    i = i + 1

print(res)
"""
