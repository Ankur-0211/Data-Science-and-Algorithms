class Solution:
    def firstUniqChar(self, s: str) -> int:
        indexMap=defaultdict(int)

        for i in s:
            if i in indexMap:
                indexMap[i]+=1
            else:
                indexMap[i]=1

        for i in range(len(s)):
            if s[i] in indexMap and indexMap[s[i]]==1:
                return i

        return -1     