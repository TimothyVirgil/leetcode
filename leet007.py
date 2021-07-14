'''
LeetCode #7: Reverse Integer
Code by Timothy Payne Jr.
Started on: July 13, 2021
Finished on: July 14, 2021
'''

def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """          
        rev_str = ''
        
        if x < 0:
            str_x = str(-x)
            
            for a in range(1,len(str_x)+1):
                rev_str += str_x[-a]
                
            rev_int = -(int(rev_str))
            
            if rev_int < -2 ** 31:                
                return 0
            
            else:                
                return rev_int                       
        
        else:  
            str_x = str(x)
            
            for a in range(1,len(str_x)+1):
                rev_str += str_x[-a]
                
            rev_int = (int(rev_str))
                
            if rev_int > (2 ** 31 - 1):
                return 0
            
            else:
                return rev_int