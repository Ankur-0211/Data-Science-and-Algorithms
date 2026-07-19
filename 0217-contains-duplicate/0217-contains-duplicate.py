class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setmap=set()

        for i in range(len(nums)):
            val=nums[i]
            if val in setmap:
                return True
            else:
                setmap.add(val)
        return False