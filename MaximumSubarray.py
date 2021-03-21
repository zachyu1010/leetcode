class Solution:
    def maxSubArray(self, nums):
        maxSum = -10 ** 5
        subSeqIdx = [0] * 2
        for idxSt in range(len(nums)):
            sum = 0
            for idxEnd in range(idxSt, len(nums)):
                sum += nums[idxEnd]
                if sum > maxSum:
                    subSeqIdx = [idxSt, idxEnd]
                    maxSum = sum
        return maxSum



            

if __name__ == "__main__":
    x = Solution()
    ans = x.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(ans)
