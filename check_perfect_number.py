# date: 01/07/2020

# Description: 
# A Perfect Number is a positive integer 
# that is equal to the sum of all its
# positive divisors except itself.

class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 0:
            return False,[]
        
        divisors = []
        for i in range(1,num):
            
            # perfect number is a positive integer 
            # that is equal to the sum of its 
            # positive divisors
            if num%i == 0:
                divisors.append(i)
        
        total = 0
        
        # double check the results
        for i in divisors:
            total+=i
            
            
        if total == num:
            return True,divisors
        else:
            return False,[]

print(Solution().checkPerfectNumber(28))
# True
# 28 = 1 + 2 + 4 + 7 + 14
