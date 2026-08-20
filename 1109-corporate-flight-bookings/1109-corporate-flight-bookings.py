class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res=[0]*n
        prefix=0

        for i in range(len(bookings)):
            l=bookings[i][0]
            r=bookings[i][1]

            res[l-1]+=bookings[i][2]
            if r<len(res):
                res[r]+=-(bookings[i][2])
        # print(res)


        for j in range(n):
            prefix+=res[j]
            res[j]=prefix
        
        return res

        