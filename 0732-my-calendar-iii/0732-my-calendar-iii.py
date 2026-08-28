class MyCalendarThree:

    def __init__(self):
        self.eventmap={}
        self.maxcount=0
        

    def book(self, startTime: int, endTime: int) -> int:
        self.eventmap[startTime]=1+self.eventmap.get(startTime,0)
        self.eventmap[endTime]=self.eventmap.get(endTime,0)-1

        sortedmap=sorted(self.eventmap.keys())
        prefix=0
        for event in sortedmap:
            prefix+=self.eventmap[event]
            self.maxcount=max(self.maxcount,prefix)
        return self.maxcount





        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)