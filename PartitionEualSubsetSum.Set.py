class Solution:
    def canPartition(self, A):
        s = sum(A)
        if s % 2 == 1:
            return False
        t = s / 2
        if A[0] == t:
            return True
        P = set([A[0]])
        for x in A[1:]:
            for y in list(P):
                m = x + y
                if t == m:
                    return True
                P.add(m)

        return False

if __name__ == "__main__":
    x = Solution()
    ans = x.canPartition([1,5,11,5])
    print(ans)
