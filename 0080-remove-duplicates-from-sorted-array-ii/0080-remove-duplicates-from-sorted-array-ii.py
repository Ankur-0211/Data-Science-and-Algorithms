class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        r=0
        while r<len(nums):
            if l<2:
                nums[l]=nums[r]
                l+=1
                
            elif nums[r]!=nums[l-1] or nums[r]!=nums[l-2]:
                nums[l]=nums[r]
                l+=1
            r+=1
        return l
        
        