class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pref = ""
        temp = ""
        word = strs[0]
        for i in range(len(word)):
            temp += word[i]
            count = 0
            for char in strs:
                if char.startswith(temp):
                    count += 1
                else:
                    pass
                if count == len(strs):
                    pref = temp
        
        return pref