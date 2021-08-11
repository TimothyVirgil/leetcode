'''
LeetCode #9: Palindrome Number
Code by Timothy Payne Jr.
Started on: August 10, 2021
Finished on: August 10, 2021
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
    
        else:

            str_num = str(x)
            rev_num = ''

            for x in range((len(str_num)-1), -1, -1):
                rev_num += str_num[x]

            if str_num == rev_num:
                return True

            else:
                return False