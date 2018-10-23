

class Solution(object):


    def threeSumMulti(self,A,target):
        """
        :param A:
        :param target:
        :return:
        """
        if not A or len(A)==0:
            return 0
        res,n,M=0 ,len(A),10**9+7
        A.sort() # // sorted()
        for i in range(n):
            l,r=i+1,n-1
            while l<r:

                    if A[i] + A[l] + A[r] == target:
                        if A[l] != A[r]:
                            left, right = 1, 1

                            while l + 1 < r and A[l] == A[l + 1]:
                                left, l = left + 1, l + 1
                            while r - 1 > l and A[r] == A[r - 1]:
                                right, r = right + 1, r - 1

                            res += left * right
                            res %= M
                            l, r = l + 1, r - 1
                        else:
                            res += (r - l + 1) * (r - l) // 2  # 例如[2,4,4]的取法
                            res %= M
                            break
                    elif A[i] + A[l] + A[r] > target:
                        r -= 1
                    else:
                        l += 1

                    return res % M