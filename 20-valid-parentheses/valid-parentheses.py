class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mem = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                mem.append(char)
            elif char == ")":
                if not mem or mem[-1] != "(":
                    return False
                mem.pop()
            elif char == "]":
                if not mem or mem[-1] != "[":
                    return False
                mem.pop()
            elif char == "}":
                if not mem or mem[-1] != "{":
                    return False
                mem.pop()
                
        return len(mem) == 0