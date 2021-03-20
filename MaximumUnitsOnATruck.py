class Solution:
        def maximumUnits(self, boxTypes, truckSize):
            getUnits = lambda x : x[1]
            boxTypes.sort(reverse = True, key=getUnits)
            maxUnits = 0
            for boxs in boxTypes: 
                for _ in range(boxs[0]): 
                    truckSize -= 1 
                    maxUnits += boxs[1]
                    if truckSize == 0:
                        break
                if truckSize == 0:
                    break
            return maxUnits

if __name__ == "__main__":
    x = Solution()
    ans = x.maximumUnits([[1,3],[2,2],[3,1]], 4)
    print(ans)
    ans = x.maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10)
    print(ans)
