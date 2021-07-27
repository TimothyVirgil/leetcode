'''
LeetCode #8: String to Integer (atoi)
Code by Timothy Payne Jr.
Started on: July 14, 2021
Finished on: July 14, 2021
'''

def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s.lstrip() #leading space delete
        s_pos = True
        str_int = ''
        
        if s == '':
            return 0
                    
        if s[0] == '-':
            s_pos = False
                        
        if s[0] == '-' or s[0] == '+':
            s = s[1::]
            
        for a in s:            
            try:
                int(a)
                str_int += a
                
            except:                
                break
                
        if str_int == '':
            return 0
        
        str_int = int(str_int)
        
        if s_pos == True and str_int < (2**31 - 1):
            return str_int
        
        elif s_pos == True:
            return (2**31 - 1)
        
        elif s_pos == False and str_int < (2**31):
            return -str_int
        
        else:
            return (-2 ** 31)
