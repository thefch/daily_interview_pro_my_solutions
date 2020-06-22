# date: 17/06/2020

def find_primes(n):
    if n < 1:
        return []
    
    # list of integer till n
    nums = [i for i in range(n)]
    for i in range(n):
        for j in range(n):

            # skip all numbers that are multiplied with 1,
            # it will remove all non-prime numbers
            if j is not 1 and i is not 1 and i*j in nums:    
                nums.remove(i*j)

            # exception for 1x1 that is not prime
            elif i==1 and j ==1:
                nums.remove(i*j)

    return nums

print(find_primes(14))
