# date: 13/07/2020

# Description:
# Given a list of numbers of size n, where n is greater than 3, 
# find the maximum and minimum of the list using less than 2 * (n - 1) comparisons.

import sys
def find_min_max(nums):
    num_of_operations = 2*(len(nums)-1)
    print('max number of operations:',num_of_operations)

    mi = sys.maxsize
    ma = 0
    i=0
    count=0
    done = False

    while not done:
        if nums[i]>ma:
            ma = nums[i]
            count+=1
        elif nums[i] < mi:
            mi = nums[i]
            count+=1

        
        
        i +=1
        if i == len(nums):
            done = True


    print('number of operations made:',count)
    return mi,ma


print(find_min_max([3, 5, 1, 2, 4, 8]))
# (1, 8)

print(find_min_max([0,5,1, 2]))
# (0, 5)