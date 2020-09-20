# PROJECT EULER - PROBLEM 1 (SOLUTION PROPOSAL)

# If we want to generalize to any number of divisors
# (provided that divisors < n)
def multipleOf(n, *divisors):
    for div in divisors:
        if n%div == 0:
            return True
    return False

# most straight-forward answer to the problem
def multipleOf3or5(n):
    return n%3==0 or n%5==0

sum = 0
N = 1000
for i in range(0, N):
    #if(multipleOf(i, 3, 5)):
    if(multipleOf3or5(i)):
       sum = sum + i

print(sum)
