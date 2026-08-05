class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        news = s[::-1]
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        output = roman[news[0]]
        for i in range(1,len(s)):
            if roman[news[i-1]] > roman[news[i]]:
                output -= roman[news[i]]
            else:
                output += roman[news[i]]

        return output