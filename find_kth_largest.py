# date: 24/06/2020

# Description:
# Find the k-th largest number in a sequence 
# of unsorted numbers.



def findKthLargest(arr, k):
  arr.sort()
  return arr[-k]
     
print(findKthLargest([8, 7, 2, 3, 4, 1, 5, 6, 9, 0], 3))
# 7
