class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_=defaultdict(int)
        for i in range(len(nums)):
            val=nums[i]
            diff=target-val
            if diff in dict_:
                return(dict_[diff],i)
            else:
                dict_[val]=i
        return []
        