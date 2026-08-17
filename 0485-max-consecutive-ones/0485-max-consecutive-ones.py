class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxOne=0
        l=0
        while l<len(nums):
            if nums[l]==1:
                count+=1
                maxOne=max(maxOne,count)
            else:
                count=0
            l+=1
        return maxOne
        