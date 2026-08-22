class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        Snums=sorted(nums)
        bestsum=Snums[0]+Snums[1]+Snums[len(Snums)-1]

        for i in range(len(Snums)): 
            l=i+1
            r=len(Snums)-1 

            while l<r:
                currentsum=Snums[i]+Snums[l]+Snums[r]

                if currentsum==target:
                    return currentsum

                elif abs(target-currentsum)<abs(target-bestsum):
                    bestsum=currentsum
                # else:
                #     r-=1
                
                if currentsum<target:
                    l+=1
                else:
                    r-=1
        return bestsum



