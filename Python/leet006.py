'''
LeetCode #6: ZigZag Conversion
Code by Timothy Payne Jr.
Started on: July 8, 2021
Finished on: July 12, 2021

'''
#could use a while condition to change if we are going up or down rows.
#store our rows as strings


def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:        
        return s #the one row case
        
    zig_list = []
    zig_it = 0
    zig_dir = 'down'
    zig_str =''

    for a in range(numRows):
        zig_list.append('') #set up our stings

    for x in s:
        zig_list[zig_it] += x

        if zig_dir == 'up' and zig_it == 0:
	        zig_dir = 'down'

        elif zig_dir == 'down' and zig_it == (numRows - 1):
	        zig_dir = 'up'

        if zig_dir == 'up':
	        zig_it -= 1

        else:
                zig_it += 1


    for b in zig_list:
        zig_str += b

    return zig_str
        

