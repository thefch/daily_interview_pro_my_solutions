# date: 22/06/2020

# Description:
# Given a list of numbers and a target number,
# find all possible unique subsets of the list 
# of numbers that sum up to the target number. 
# The numbers will all be positive numbers.

# return the total of an array
def get_total(nums):
  total = 0
  for i in nums:
    total += i
  return total  


def sum_combinations(nums, target):
    final = []

    for i in range(1,len(nums)):
        lst = [nums[i]]
        for j in range(1,len(nums)):
            if i !=j:
                # check if the number can be added
                if nums[j] + get_total(lst) <= target:
                    lst.append(nums[j])

        # check if the list has been found
        if get_total(lst) == target:
            final.append(lst)
            lst = []
    return final



print(sum_combinations([10, 1, 2, 7, 6, 1, 5], 8))
# [(2, 6), (1, 1, 6), (1, 2, 5), (1, 7)]
