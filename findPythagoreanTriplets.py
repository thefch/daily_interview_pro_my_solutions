#date: 20/06/2020

import math
def findPythagoreanTriplets(nums):
    # list with the squared nums
    list = [i**2 for i in nums]
    
    for i in range(0,len(list),1):
        for j in range(0,len(list),1):
        
            #triplet total
            total = list[j] + list[i]
            
            # it must not check its self
            # if the totla is in the list, triplet exists
            if (total) in list and (i is not j):
                
                print('=> {}**2 + {}**2 = {}**2'.format(nums[j],nums[i],int(math.sqrt(total))))
                print('=> {} + {} = {}'.format(list[j],list[i],total))
                return True
    return False

print (findPythagoreanTriplets([3, 12, 5, 13]))
