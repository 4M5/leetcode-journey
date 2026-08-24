class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ndigit = int("".join(map(str,digits)))
        plusone = ndigit + 1
        return list(map(int,str(plusone)))