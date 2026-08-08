class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        prefixsum=[0]*len(nums)
        prefixsum[0]=nums[0]
        prefix_freq={0:1}

        for i in range(1,len(nums)):
            prefixsum[i]=prefixsum[i-1]+nums[i]
        
        for j in range(len(nums)):
            sumval=prefixsum[j]
            diff=sumval-k
           
            if diff in prefix_freq:
                res+=prefix_freq[diff]
                
            prefix_freq[sumval] =1+prefix_freq.get(sumval,0)
        
        return res
                



        


            