class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        n=len(mat)
        middle=0
        for i in range(n):
            for j in range(n):
                if i==j:
                    sum+=mat[i][j]
                if i+j == n-1:
                    sum+=mat[i][j]
                middle=mat[n//2][n//2]
        if n%2!=0:
            sum=sum-middle
        return sum
        