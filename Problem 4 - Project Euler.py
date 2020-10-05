# PROJECT EULER - PROBLEM 4 (SOLUTION PROPOSAL)

# check if it is a palindrome
def isPalindrome(n):
    num_txt = str(n)
    return num_txt == num_txt[::-1]

# simple solution (not the fastest)
def getLargestPalindrome():
    largest = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            num = i*j
            if isPalindrome(num) and num > largest:
                    largest = num
    return largest

print(getLargestPalindrome())
