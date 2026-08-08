class Solution:
    def isValid(self, s: str) -> bool:
        valid=True
        stack =[]
        if not len(s) % 2 ==0:
            return False
        else:    
            for i in s:
                if i == "[" or i=="{" or i== "(":
                    stack.append(i)

                else:
                    if stack ==[]:
                        valid= False
                        break 
                    else:
                        if i=="]":
                            if not stack.pop() == "[":

                                valid = False
                                break
                            
                        if i=="}":
                            if  not stack.pop() == "{":
                                valid = False
                                break
                                
                        if i==")":
                            if  not stack.pop() == "(":
                                valid = False
                                break
        if not stack ==[]:
            return False
        else:
            return valid
                        