# PROJECT EULER - PROBLEM 5 (SOLUTION PROPOSAL)

N = 10
x = N+1

# get primes (heavy way)
def get_primes_until(n):
    primes = []
    primes.append(1)
    for i in range(1, n):
        isPrime = True
        if i > 1:  
            for j in range(2, i):
                if i%j == 0:
                    isPrime = False
            if isPrime == True:
                primes.append(i)
    return primes

primes = get_primes_until(N)

while(True):
    evenly_prime = True
    # only has to test for prime numbers
    for i in primes:
        if x%i != 0:
            evenly_prime = False
            break
    if evenly_prime == True:
        break

print(x)
