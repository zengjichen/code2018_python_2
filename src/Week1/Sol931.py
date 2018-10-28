"""

sol932 jichenzeng fork form github idea

"""

class Solution:
    def minFallingPathSum(self, A):
        for i in range(1, len(A)):
            for j in range(len(A)):
                A[i][j] += min(A[i - 1][(j and j - 1):j + 2])   ##and return the last 全为真返回最后，否则第一个
        return min(A[-1])

def minFallingPathSum(A):
        for i in range(1, len(A)):
            for j in range(len(A)):
                #print(map(j and j-1:j+2))
                print((j-1))
                print((j+2))
                #print((j-1):(j+2))
                print(A[j])
                print("@@@@@@@@@@@@@@@”“”")
                print(A[i][j-1:j+2])
                print(j)
                print(A[i][j and j-1:j+2])

                A[i][j] += min(A[i - 1][j and j - 1:j + 2])
        return min(A[-1])

A=[[1,2,3]]*3

print(minFallingPathSum(A))