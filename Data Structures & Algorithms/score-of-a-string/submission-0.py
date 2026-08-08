class Solution:
    def scoreOfString(self, s: str) -> int:
        total=0
        for i in range(0,len(s)-1):
            difference =  ord(s[i])-ord(s[i+1])
            if difference<0:
                difference*=-1
            total+=difference


        return total