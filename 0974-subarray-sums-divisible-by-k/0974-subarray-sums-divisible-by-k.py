class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq={0:1}

        prefix=0
        count=0

        for i in range(len(nums)):
            prefix+=nums[i]
            rem=prefix % k
            
            if rem in freq:

                count+=freq[rem]

            freq[rem]=1+freq.get(rem,0)
        return count
            
        