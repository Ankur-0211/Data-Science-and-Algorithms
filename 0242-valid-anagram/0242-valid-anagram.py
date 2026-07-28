class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countMap=defaultdict(int)

        if len(s)!=len(t):
            return False

        for char in s:
            if char in countMap:
                countMap[char]+=1
            else:
                countMap[char]=1
        
        for char in t:
            if char in countMap and  countMap[char]>0:
                countMap[char]-=1
            else:
                return False
        return True
            
        