class Solution:
    def areAlmostEqual(self, s1, s2):
        strlen = len(s1)
        pos = []
        for i in range(0, strlen):
            if s1[i] == s2[i]:
                continue
            pos.append(i)
       
        if len(pos) == 0:
            return True
        if len(pos) == 2 and s1[pos[0]] == s2[pos[1]] and s1[pos[1]] == s2[pos[0]]:
            return True
        return False
    
if __name__ == "__main__":
    x = Solution();
    #ans = x.areAlmostEqual("bank", "kanb")
    #ans = x.areAlmostEqual("attack", "defend")
    ans = x.areAlmostEqual("kelb", "kelb")
    print(ans);

      

            
        
