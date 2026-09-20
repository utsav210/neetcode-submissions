class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones_found = 0
        max_ones = 0
        for num in nums:
            if num == 1:
                ones_found += 1
                max_ones = max(ones_found, max_ones)
            else:
                ones_found = 0

        return max_ones