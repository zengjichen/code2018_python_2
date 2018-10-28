class Solution(object):
    def numSubarraysWithSum(self, A, S):
        indexes = [-1] + [ix for ix, v in enumerate(A) if v] + [len(A)]
        ans = 0

        if S == 0:
            for i in range(len(indexes) - 1):
                # w: number of zeros between two consecutive ones
                w = indexes[i+1] - indexes[i] - 1    #0的个数 a【i+1】-a[i]-1
                print(w * (w+1) / 2)    # // 1+2+3+...+n=(n+1)*n/2
                ans += w * (w+1) / 2
            return ans

        for i in range(1, len(indexes) - S):
            j = i + S - 1
            left = indexes[i] - indexes[i-1]  #左边0的个数+1
            right = indexes[j+1] - indexes[j]   #右边0的个数+1
            ans += left * right
        return ans



arr=[1]+[1,2,3]+[4]  #arr=[1]+[1,2,3]+[4]  #
A=[1,0,1,0]
sol= Solution()
res=sol.numSubarraysWithSum(A,0)
print(res)

indexes = [-1] + [ix for ix, v in enumerate(A) if v] + [len(A)]
print(indexes)




"""
et P[i] = A[0] + A[1] + ... + A[i-1]. 
Then P[j+1] - P[i] = A[i] + A[i+1] + ... + A[j],
the sum of the subarray [i, j].

Hence, we are looking for the number of i < j with P[j] - P[i] = S.
"""
import  collections
class Solution2(object):
    def numSubarraysWithSum(self, A, S):
        P = [0]
        for x in A:
            P.append(P[-1] + x)
        count = collections.Counter()

        ans = 0
        for x in P:
            ans += count[x]
            count[x + S] += 1

        return ans







P = [0]
for x in A:
    P.append(P[-1] + x)
count = collections.Counter()
A=[1,0,1,0]
ans = 0
print(P)
for x in P:

    print(count)
    ans += count[x]
    count[x + 2] += 1
print(count)






