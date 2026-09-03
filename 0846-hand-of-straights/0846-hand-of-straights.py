class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n % groupSize!=0:
            return False
        freq={}

        hand.sort()

        for i  in hand:
            freq[i]=1+freq.get(i,0) 

        for i in hand:
            if freq[i]!=0:
                for j  in range(groupSize):
                    current=i+j
                    if current in freq and freq[current]>0:

                        freq[current]-=1
                    else:
                        return False

        
        for card in freq:
            if freq[card]>0:
                return False
        
        return True
        