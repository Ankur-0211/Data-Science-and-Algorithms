class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix=0
        remaindermap={0:-1}

        for i in range(len(nums)):
            prefix+=nums[i]
            remainder=prefix%k

            if remainder not in remaindermap:
                remaindermap[remainder]=i
            elif i-remaindermap[remainder]>1:
                return True
        
        return False