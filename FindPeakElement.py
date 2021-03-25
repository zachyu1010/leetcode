class Solution:
    def findPeakElement(self, nums):
        l = 0
        m = 1
        r = len(nums) - 1
        if r == 0:
            return 0
        elif nums[0] > nums[1]:
            return 0
        elif nums[r] > nums[r - 1]:
            return r
        while True:
            if nums[m - 1] < nums[m] and nums[m] > nums[m + 1]:
                return m
            elif nums[m] < nums[l] or nums[m - 1] > nums[m]:
                r = m
            else:
                l = m
            m = (l + r) // 2

if __name__ == "__main__":
    x = Solution()
    ans = x.findPeakElement([1, 2, 3, 4, 3]);
    print(ans)
    ans = x.findPeakElement([0, 1, 0]);
    print(ans)
    ans = x.findPeakElement([24,69,100,99,79,78,67,36,26,19]);
    print(ans)
