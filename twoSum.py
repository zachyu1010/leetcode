class Solution:
    def twoSum(self, nums, target):
        loop = len(nums);
        for i in range(0, loop ):
            try: 
                return (i, i+1+nums[i+1:loop].index(target - nums[i]))
            except:
                pass

if __name__ == "__main__":
    x = Solution()
    ans = x.twoSum([-1, -2, -3, -4, -5], -8)
    print(ans);
