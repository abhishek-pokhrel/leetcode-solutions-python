'''
3251. Find the Count of Monotonic Pairs II

You are given an array of positive integers nums of length n.

We call a pair of non-negative integer arrays (arr1, arr2) monotonic if:

The lengths of both arrays are n.
arr1 is monotonically non-decreasing, in other words, arr1[0] <= arr1[1] <= ... <= arr1[n - 1].
arr2 is monotonically non-increasing, in other words, arr2[0] >= arr2[1] >= ... >= arr2[n - 1].
arr1[i] + arr2[i] == nums[i] for all 0 <= i <= n - 1.

Return the count of monotonic pairs.
'''

class Solution(object):
    def countOfPairs(self, nums):
        N = len(nums)
        MX = max(nums)
        MOD = 10**9+7
        dp =[[0] * (MX + 1) for _ in range(N+1)]
        dpp =[[0] * (MX + 5) for _ in range(N+1)]

        for up in range(nums[0] + 1):
            dp[0][up] = 1
            dpp[0][up + 1] = dp[0][up] + dpp[0][up]

        for index in range(1, N):
            for up in range(nums[index] + 1):
                down = nums[index] - up

                right = min(nums[index - 1] - down, nums[index - 1], up)

                dp[index][up] = (dpp[index - 1][right + 1]) % MOD

                dpp[index][up + 1] = dp[index][up] + dpp[index][up]

                dpp[index][up + 1] %= MOD

        total = 0
        for i in range(nums[N - 1] + 1):
            total += dp[N -1][i]
        return total % MOD
    
# Test case
Test = Solution()
print(Test.countOfPairs([2,3,2]))