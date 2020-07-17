# date: 10/07/2020

# Description:
# Given an array of numbers, determine whether it
# can be partitioned into 3 arrays of equal sums

# For instance,
# [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1] can be partitioned into:
# [0, 2, 1], [-6, 6, -7, 9, 1], [2, 0, 1] all of which sum to 3


class Solution(object):
    def canThreePartsEqualSum(self, A):
        total = 0
        lst = []
        vals = []
        for a in A:
            total += a
            vals.append(a)
            if total == 3:
                lst.append(vals)
                total = 0
                vals = []

            if total > 3:
                return False
        
        print('lst out:',lst)
        return True
            
                
print(Solution().canThreePartsEqualSum(
    [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
# True