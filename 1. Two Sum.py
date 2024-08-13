'''
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {} # value: index

        for i, num in enumerate(nums):
            difference = target - num
            if difference in prevMap:
                return [prevMap[difference], i]
            prevMap[num] = i
        return