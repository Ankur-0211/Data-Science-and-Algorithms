class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        Snums=sorted(nums)
        res=[]
        

        for i in range(len(Snums)):

            if i>0 and Snums[i]==Snums[i-1]:
                    continue

            total=0
            l,r=i+1,len(Snums)-1
            while l<r:
                total=Snums[i]+Snums[l]+Snums[r]
                if total==0:
                    res.append([Snums[i],Snums[l],Snums[r]])
                    l+=1
                    r-=1

                    while l<r and Snums[l]==Snums[l-1]:
                        l+=1
                    while l<r and Snums[r]==Snums[r+1]:
                        r-=1
                
                
                elif total<0:
                    l+=1
                else:
                    r-=1
        print(res)
        
        return res
