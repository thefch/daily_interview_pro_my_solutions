# date: 19/06/2020

# Description:
# Given an array of n positive integers and a positive integer s, 
# find the minimal length of a contiguous subarray of which the sum ≥ s.
# If there isn't one, return 0 instead.

# return the total of an array
def get_total(nums):
  total = 0
  for i in nums:
    total += i
  return total       

def minSubArrayLen( nums, s):
  final = []

  for i in range(1,len(nums)):
    lst = [nums[i]]
    for j in range(1,len(nums)):

      # check if the number can be added
      if nums[j] + get_total(lst) <= s:
        lst.append(nums[j])

    # check if the list has been found
    if get_total(lst) == s:
      final.append(lst)
      lst = []

  if len(final) == 0:
    return []

  temp = len(final[0])
  out = final[0]

  # find the smalletst in length combination
  for i in final:
    if len(i)< temp:
      out = i
      
  return out


print(minSubArrayLen([2, 3, 1, 2, 4, 3], 7))