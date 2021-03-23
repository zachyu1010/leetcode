class Solution:
    def peakIndexInMountainArray(self, arr):
        r = len(arr) - 1
        l = 0
        while True:
            m = (l + r) // 2
            if arr[m-1] < arr[m] and arr[m] > arr[m+1]:
                return m
            elif arr[m-1] < arr[m] and arr[m] < arr[m+1]:
                l = m
            else:
                r = m

if __name__ == "__main__":
    x = Solution()
    ans = x.peakIndexInMountainArray([0, 1, 0]);
    print(ans)
    ans = x.peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19]);
    print(ans)
