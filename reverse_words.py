# date: 06/09/2019

# Description:
# Given a string, you need to reverse the 
# order of characters in each word within 
# a sentence while still preserving whitespace 
# and initial word order.
class Solution:
    
    # reverse a word
    def reverse_word(self,w):
        out=''
        for i in range(len(w)-1,-1,-1):
            out +=w[i]
        return out
            
    def reverseWords(self, str):
        parts = str.split(' ')
        out = ''
        for p in parts:
            out += self.reverse_word(p)+' '
        
        return out.strip()
  
print(Solution().reverseWords("The cat in the hat"))
# ehT tac ni eht tah
