class Solution:
    def spiralOrder(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans
    

if __name__ == "__main__":
    x = Solution()
    ans = x.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(ans)
    ans = x.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    print(ans)
    ans = x.spiralOrder([[7],[9],[6]])
    print(ans)
