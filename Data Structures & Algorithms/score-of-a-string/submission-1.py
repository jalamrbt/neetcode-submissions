class Solution:
    def scoreOfString(self, s: str) -> int:
        total=0
        for i in range(0,len(s)-1):
            difference = abs(ord(s[i])-ord(s[i+1]))
        
            total+=difference


        return total