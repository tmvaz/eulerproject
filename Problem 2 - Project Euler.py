# PROJECT EULER - PROBLEM 2 (SOLUTION PROPOSAL)

# this version for the fibonacci function
# uses a rudimentary form of "memoizing - without a dictionary
series = [1, 2]
def fibo(n):
    if n > 0:
        if n<3:
            return series[n-1]
        elif n <= len(series):
            return series[n-1]
        else:
            series.append(fibo(n-1) + fibo(n-2))
            return series[-1]

i = 1
res = 0
z = 0
while(z < 4000000):
    z = fibo(i)
    if z%2 == 0:
        res = res + z
    i = i + 1

print(res)
