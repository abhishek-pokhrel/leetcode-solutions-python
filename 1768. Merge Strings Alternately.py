'''
1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
'''

class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged = ''
        length = min(len(word1), len(word2))
        
        for i in range(length):
            merged += word1[i] + word2[i]
        
        merged += word1[length:] + word2[length:]
        return merged
    
## Test Case
Test = Solution()
print(Test.mergeAlternately('abc', 'pqr'))