class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dict_=defaultdict(int)
        ans=[]
        for i in nums:
            if i in dict_:
                dict_[i]+=1
            else:
                dict_[i]=1

        for i in range(len(nums)):
            if i+1 not in dict_:
                ans.append(i+1)
            else:
                continue
        return ans    