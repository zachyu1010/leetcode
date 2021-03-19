class Solution:
    def spiralOrder(self, matrix):
        next_dir = [1, 2, 3, 0]
        dir = 0
        s = []
        seq = []
        rlen = len(matrix)
        while(rlen):
            if dir == 0: 
                s = matrix.pop(0)
            elif dir == 1:
                if len(matrix[0]) == 1:
                    s = [matrix.pop(0)[0] for i in range(rlen)]
                else:
                    s = [matrix[i].pop() for i in range(rlen)] 
            elif dir == 2:
                s = matrix.pop()
                s.reverse()
            elif dir == 3:
                if len(matrix[0]) == 1:
                    s = [matrix.pop()[0] for i in range(rlen)] 
                else: 
                    s = [matrix[i].pop(0) for i in range(rlen)]
                    s.reverse()
            seq = seq + s
            dir = next_dir[dir]
            rlen = len(matrix)

        return seq 
    

if __name__ == "__main__":
    x = Solution()
    ans = x.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(ans)
    ans = x.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    print(ans)
    ans = x.spiralOrder([[7],[9],[6]])
    print(ans)
