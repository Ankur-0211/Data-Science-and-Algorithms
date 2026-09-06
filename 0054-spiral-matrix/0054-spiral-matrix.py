class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        L,T=0,0
        R,B=len(matrix[0]),len(matrix)
        res=[]

        while L<R and T<B:
            for l in range(L,R):
                res.append(matrix[T][l])
            T+=1

            for d in range(T,B):
                res.append(matrix[d][R-1])
            R-=1
            if T<B:
                for r in range(R-1,L-1,-1):
                    res.append(matrix[B-1][r])
                B-=1

            if L<R:

                for u in range(B-1,T-1,-1):
                    res.append(matrix[u][L])
                L+=1
        return res
