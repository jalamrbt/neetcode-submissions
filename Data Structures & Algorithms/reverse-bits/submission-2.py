class Solution:
    def reverseBits(self, n: int) -> int:
        
        n = format(n, '032b')
        new =""

        for i in range(0,32):
            new+= str(n[31-i])
        
        return(int(new,2))