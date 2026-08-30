class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def counter(mid: int)->int:
            l=0
            r=1
            totalpair=0

            while r<len(nums):
                
                while nums[r]-nums[l]>mid: 
                    l+=1
                totalpair+=r-l
                r+=1
            return totalpair

        lower=0
        upper=max(nums)

        while lower!=upper:
            mid=(lower+upper)//2

            pair=counter(mid)

            if pair>=k:
                upper=mid
            elif pair<k:
                lower=mid+1
        
        return lower 


        
        
        
        
                

        