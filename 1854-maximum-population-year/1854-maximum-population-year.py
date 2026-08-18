class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        maxyear=0
        maxpop=0
        pop=0
        event={}

        for i in range(len(logs)):
            birth=logs[i][0]
            death=logs[i][1]

            event[birth]=1+event.get(birth,0)
            event[death]=event.get(death,0)-1
        

        years=sorted(event.keys())

        for year in years:
            pop+=event[year]

            if pop>maxpop:
                maxpop=pop
                maxyear=year
        return maxyear

            
        