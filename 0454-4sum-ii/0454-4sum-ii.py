class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sumMap={}
        pair_sum=0
        for i in nums1:
            
            for j in nums2:
                pair_sum=i+j
                sumMap[pair_sum]=1+sumMap.get(pair_sum,0)
        
        count=0

        for k in nums3:
            
            for l in nums4:
                if -(k+l) in sumMap:
                    count+=sumMap[-(k+l)]
                    
        
        return count