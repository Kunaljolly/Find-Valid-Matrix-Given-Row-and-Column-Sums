class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        t = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                t[i][j] = min(rowSum[i],colSum[j])
                rowSum[i] -= t[i][j]
                colSum[j] -= t[i][j]


        return t
