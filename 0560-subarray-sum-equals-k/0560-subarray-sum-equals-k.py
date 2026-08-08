class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # res=0
        # prefixsum=[0]*len(nums)
        # prefixsum[0]=nums[0]
        # prefix_freq={0:1}

        # for i in range(1,len(nums)):
        #     prefixsum[i]=prefixsum[i-1]+nums[i]
        
        # for j in range(len(nums)):
        #     sumval=prefixsum[j]
        #     diff=sumval-k
           
        #     if diff in prefix_freq:
        #         res+=prefix_freq[diff]

        #     prefix_freq[sumval] =1+prefix_freq.get(sumval,0)
        
        # return res

        res=0
        prefix=0
        prefixmap={0:1}


        for i in range(len(nums)):
            prefix+=nums[i]
            diff=prefix-k

            res+=prefixmap.get(diff,0)

            prefixmap[prefix]=prefixmap.get(prefix,0)+1
        return res

                



        


            