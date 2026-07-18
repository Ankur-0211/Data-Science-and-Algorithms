class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_=defaultdict()
        ans=[]

        for word in strs:
            sortedword=''.join(sorted(word))
            if sortedword in dict_:
                valuelist=dict_[sortedword]
                valuelist.append(word)
                dict_[sortedword]=valuelist
            else:
                valuelist=[]
                valuelist.append(word)
                dict_[sortedword]=valuelist

        for key in dict_:
            ans.append(dict_[key])      
        
        return ans

                
        