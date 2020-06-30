# date: 12/07/2019

# Description:
# Given a string, find the length of 
# the longest substring without repeating characters.

class Solution(object):
  def lengthOfLongestSubstring(self, s):
        strs = []
        out = ''
        for i in s:
            if i not in out:
                out +=i
            else:
                strs.append(out)
                out =''
        strs.append(out)
        strs = sorted(strs, key=len)
        highest = len(strs[-1])
        
        lst = [i for i in strs if len(i)==highest]
        return lst
  
print(Solution().lengthOfLongestSubstring('abcdabcddefgh'))