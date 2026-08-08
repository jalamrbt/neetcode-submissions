class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        spointer =0
        tpointer =0
        found = False
        if s==t:
            found=True   
        
        for x in range(0,len(t)):
            if(spointer<len(s) and s[spointer]==t[tpointer] ):
                spointer+=1
            
            tpointer+=1
            if spointer == len(s):
                found = True
                break

        return found