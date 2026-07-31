class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        letter=""
        l=0
        r=len(s)-1

        while l<r:
            letter=s[l]
            s[l]=s[r]
            s[r]=letter
            l+=1
            r-=1