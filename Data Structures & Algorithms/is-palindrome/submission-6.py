class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = True
        startPointer = 0
        endPointer = len(s)-1

        while startPointer<len(s) and endPointer>-1:
            
            while (startPointer<len(s) and endPointer>-1 and (s[startPointer].isalnum() is False or s[endPointer].isalnum() is False)) : 
               
                if s[startPointer].isalnum() is False:
                    startPointer+=1
                if s[endPointer].isalnum() is False:
                    endPointer-=1

            if (startPointer<len(s) and endPointer>-1) and s[startPointer].lower() != s[endPointer].lower():
                palindrome = False
                break

            startPointer+=1
            endPointer-=1                    

        return palindrome
        