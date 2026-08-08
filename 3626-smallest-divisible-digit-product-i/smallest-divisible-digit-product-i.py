class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            prod = 1
            for i in str(n):
                prod *= int(i)
            if prod%t == 0:
                return n
            else:
                 n += 1
            
