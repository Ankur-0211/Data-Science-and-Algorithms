class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        res=[0]*100000

        for i in range(len(trips)):
            f=trips[i][1]
            t=trips[i][2]

            res[f]+=trips[i][0]
            res[t]-=trips[i][0]
        prefix=0
        for i in range(len(res)):
            prefix+=res[i]
            res[i]=prefix

            if res[i]>capacity:
                return False
        
        return True

            
        