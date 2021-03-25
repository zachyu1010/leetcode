class Solution:
    def canPartition(self, nums):
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for n in nums:
            if n > target:
                continue
            for i in range(target, -1, -1):
                if dp[i] == True:
                    if target >= i + n:
                        dp[i + n] = True
        return dp[target]



if __name__ == "__main__":
    x = Solution()
    ans = x.canPartition([1,5,11,5])
    print(ans)
    ans = x.canPartition([1,2,5])
    print(ans)
