class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        dirty = [[0 for col in range(n)] for row in range(m)]
        # 0: right, 1: down, 2: left, 3:top
        next_dir = [1, 2, 3, 0]
        dir = 0
        seq = []
        x = y = 0
        for i in range(0, m*n):
            seq.append(matrix[x][y])
            dirty[x][y] = 1;
            if dir == 0:
                y = y + 1;
            elif dir == 1:
                x = x + 1;
            elif dir == 2:
                y = y - 1;
            else: 
                x = x - 1;

            #check if need to change direction
            if 0 <= x and x < m and 0 <= y and y < n and dirty[x][y] == 0:
                pass
            else:
                dir = next_dir[dir]
                if dir == 0:
                    x = x + 1
                    y = y + 1
                elif dir == 1:
                    x = x + 1
                    y = y - 1
                elif dir == 2:
                    x = x - 1
                    y = y - 1
                else:
                    x = x - 1
                    y = y + 1
        return seq  

            

if __name__ == "__main__":
    x = Solution()
    #ans = x.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ans = x.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    print(ans)
