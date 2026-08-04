class Solution:
    def validPalindrome(self, s: str) -> bool:

        def palindrome(left:int,right:int)-> bool:

            while left<right:
                while left<right and not s[left].isalnum():
                    left+=1
                while left<right and not s[right].isalnum():
                    right-=1
                
                if s[left]!=s[right]:
                    return False
                
                left+=1
                right-=1
            return True
        
        l=0
        r=len(s)-1

        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            
            if s[l]!=s[r]:
                return(palindrome(l,r-1) or palindrome(l+1,r))
            
            l+=1
            r-=1
        return True

                    
                
        