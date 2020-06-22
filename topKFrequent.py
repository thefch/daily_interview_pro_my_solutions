# date: 14/06/2020

# Given a non-empty list of words, return the k most frequent words. 
# The output should be sorted from highest to lowest frequency, 
# and if two words have the same frequency, the word with lower alphabetical order comes first. 
# Input will contain only lower-case letters.


class Solution(object):
    def topKFrequent(self, words, k):

        # create a dictionary with each word and 0 as counter
        words_dict = dict.fromkeys(words,0)

        # update each counter
        for i in words: 
            words_dict[i] += 1

        # sort the dictionary
        words_dict_sorted = sorted(words_dict.items(), key=lambda x: x[1],reverse=True)     

        lst = []
        # return a list with the k words
        for i in range(k):
            lst.append(words_dict_sorted[i][0])

        return lst
        
        
words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']
