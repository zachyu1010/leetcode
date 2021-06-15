class Solution:
    def createSortedArray(self, instructions):
        maxvalue = max(instructions) #find the maximum value from the list
        nodes = [0]*(maxvalue+1) #build a list with (maxvalue+1) numbers, the range is from [0, maxvalue]
        #nodes[x] stands for the occurence of the number x in instructions, so we put 0 by default

        def query(x): #get the occurence sum of [0,x] range numbers
            res = 0
            while x > 0:
                res += nodes[x]
                x -= x&-x
            return res

        def update(x): #add 1 occurence for the number x, so we need to update all ranges containing it
            while x <= maxvalue:
                nodes[x] += 1
                x += x&-x

        count = 0
        for idx, x in enumerate(instructions):
            left = query(x-1) # the total occurences of numbers smaller than x
            right = idx - query(x) # the total occurences of numbers bigger than x
            count += min(right, left)
            update(x)
        return count%(10**9 + 7)


if __name__ == "__main__":
    x = Solution()
    ans = x.createSortedArray([9,9,9,7,7,5,5,3,3,1,1,1])
    print(ans)
    ans = x.createSortedArray([1,3,3,3,2,4,2,1,2])
    print(ans)

