class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        max_area=0
        
        while l<r:
            if height[l]<height[r]:
                
                area=min(height[l],height[r])*(r-l)
                l+=1

            else:
                area=min(height[l],height[r])*(r-l)
                r-=1

            max_area=max(area,max_area)
        return max_area