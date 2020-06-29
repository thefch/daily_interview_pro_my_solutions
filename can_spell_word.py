# date: 28/06/2020

# Description:
# A criminal is constructing a ransom note.
#  In order to disguise his handwriting, 
# he is cutting out letters from a magazine.
# Given a magazine of letters and the note he wants to write,
# determine whether he can construct the word.


class Solution(object):
    def canSpell(self, magazine, note):
        word = list(note)
      
        for i in word:
            if i in magazine:
                magazine.remove(i)
            else:
                return False
        return True

         
    
print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
# True

print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
# False