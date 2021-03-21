class Solution:
    def maxSubArray(self, nums):
        maxSeqSum = subSeqSum = nums[0] 
        subSeqIdx = [0] * 2
        idxSt = idxEnd = 0
        maxIdxSt = maxIdxEnd = 0
        for i in range(1, len(nums)):
            if subSeqSum + nums[i] > nums[i]:
                subSeqSum += nums[i] 
                idxEnd = idx
            else:
                subSeqSum = nums[i]
                idxSt = idxEnd = i
                
            if subSeqSum > maxSeqSum:
                maxSeqSum = subSeqSum
                maxIdxSt, maxIdxEnd = idxSt, idxEnd
         return maxSeqSum 


if __name__ == "__main__":
    x = Solution()
    ans = x.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(ans)
