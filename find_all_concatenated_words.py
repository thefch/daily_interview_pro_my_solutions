# date: 17/07/2020

# Description:
# Given a set of words,
# find all words that are concatenations of other words in the set.




class Solution(object):            
    def findAllConcatenatedWords(self, words):
        seen = []
        wrds = []
        for i,a in enumerate(words):
            for j,b in enumerate(words):
                
                # don't check the same string
                if i != j:
                    # check if the string is in the words list, and has not checked before
                    if a+b in words and a+b not in seen:
                        wrds.append(a+b)
                        seen.append(a+b)
                    
        return wrds
          
      
      


input = ['rat', 'cat', 'cats', 'dog', 'catsdog', 'dogcat', 'dogcatrat']
print(Solution().findAllConcatenatedWords(input))
# ['catsdog', 'dogcat', 'dogcatrat']