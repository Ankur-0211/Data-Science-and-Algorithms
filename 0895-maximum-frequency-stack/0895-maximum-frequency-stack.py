class FreqStack:

    def __init__(self):
        self.maxCount=0
        self.cntMap={}
        self.stacks={}
        

    def push(self, val: int) -> None:
        valcnt=1+self.cntMap.get(val,0)
        self.cntMap[val]=valcnt

        if valcnt>self.maxCount:
            self.maxCount=valcnt
            self.stacks[valcnt]=[]
        self.stacks[valcnt].append(val)


        

    def pop(self) -> int:
        res=self.stacks[self.maxCount].pop()
        self.cntMap[res]-=1
        
        if not self.stacks[self.maxCount]:
            self.maxCount-=1

        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()