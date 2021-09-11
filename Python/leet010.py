def string_comp(s,p):        
        
    def let_check(a,b):
                if a == b or a == '.':
                    return True
                else:
                    return False

    if '*' not in p: # no stars just check each letter
        if len(p) != len(s):
            return False

        else:
            for x in range(len(p)):
                if let_check(p[x],s[x]):
                    continue
                else:
                    return False
            else:
                return True

    elif '*' in p and p[-1] != '*': #quick backend check... maybe take out?
        if s[-1] != p[-1] and p[-1] != '.':
            return False


    star_indices = {} #this makes a dictionary of indices of star characters with their current count attempt      

    for a in range(len(p)): #list of star_indices - 0 index count, 1 index - s location
        if p[a] == '*':
            star_indices[a-1-len(star_indices)] = [-1,-1]

    highest_active = -1 #active status, -1 means no stars active yet

    index_list = sorted(list(star_indices.keys()))
    #make a string without stars

    b=''
    for a in p:
        if a != '*':
            b += a

    s_ind = 0
    b_ind = 0
    highest_ind = 0
    bob = 0
    control = 'a'  

    while s_ind < len(s) and b_ind < len(b): #iter through strings until we go past the end of one of them
        bob += 1
        
        print(highest_active,b_ind,s_ind,highest_ind,s[s_ind],b[b_ind])
        print('begin of loop')
        print(star_indices)             

        if b_ind in star_indices.keys(): #need to come up with specific criteria if it is the last index
            print('hi')           

            if b_ind == len(b)-1: #if we are on the final index point
                print('hi2')

                #check if first star
                if highest_active == -1:
                    print('hi3')

                    if let_check(b[b_ind], s[s_ind]):
                        print('hi4')

                        if s_ind == (len(s)-1):
                            print('hi5')
                            s_ind += 1
                            b_ind += 1
                            break
                        else:
                            s_ind += 1
                            print('hi6')
                            continue

                    else: #need to double check but pretty sure if is the first with no match we are screwed
                        print('hi40')
                        return False

                    '''elif highest_active == 0:  # we are on the 2nd star
                    highest_active += 1
                    highest_ind = index_list[highest_active]
                    star_indices[b_ind][0] = 0
                    star_indices[b_ind][1] = s_ind
                    print('hi41')
                    continue'''

                else:
                    print('hi7')                   

                    if let_check(b[b_ind],s[s_ind]):

                        if s_ind == (len(s)-1): #end of s string
                            print('hi8')
                            s_ind += 1
                            b_ind += 1
                            break

                        else: #try s until end
                            s_ind += 1
                            print('hi9')
                            continue

                    else: #go back to last star and try again
                        print('hi10')                       
                        
                        highest_ind = index_list[highest_active]
                        b_ind = highest_ind
                        s_ind = star_indices[highest_ind][1]
                                               
                        print(b_ind,s_ind)
                        continue

            else: #star but not in the final position                

                if highest_active == -1: #first star
                    print('hi20')
                    star_indices[b_ind][0] = 0 #set count to 0           
                    star_indices[b_ind][1] = s_ind #set corresponding s_index
                    b_ind += 1 #move to next index
                    highest_active += 1 #move to next highest on list
                    highest_ind = index_list[highest_active]
                    continue

                else: #not the first star

                    if star_indices[b_ind][0] == -1: #first time getting to this star
                        highest_active += 1
                        highest_ind = index_list[highest_active]
                        print('hi25')
                        star_indices[b_ind][0] = 0
                        star_indices[b_ind][1] = s_ind
                        b_ind += 1
                        continue

                    elif star_indices[b_ind][0] == 0: #current count 0
                        print('hi21')
                        d = b_ind
                        e = s_ind           

                        if let_check(b[d], s[e]):
                            print('hi22')
                            star_indices[b_ind][1] = s_ind + 1
                            star_indices[b_ind][0] = 1                                               
                            b_ind  += 1 # set my index to next b 
                            s_ind  += 1 # set my index to next s

                            #store the next index to check in case we get to 2                            
                            continue

                        #failed one time check
                        else:
                            print('hi23')
                            if highest_active == 0: #first star has failed 0 and 1
                                return False
                            #not the first star
                            #go back and check last star
                            else:

                                print('hi24')
                                print(highest_ind,b_ind)
                                star_indices[highest_ind][0] = -1                               
                                highest_active -= 1 #need to check last active
                                highest_ind = index_list[highest_active]
                                b_ind = highest_ind
                                s_ind = star_indices[highest_ind][1]
                                continue
                    #we passed a one check already with this star
                    elif star_indices[b_ind][0] >= 1:# increase by 1 and try
                        print('hi29')                        
                        d = b_ind
                        e = star_indices[b_ind][1]                                                
                        #if it works, set the new count and index, increase b and s by 1
                        if let_check(b[d], s[e]): #check the increased by 1
                            star_indices[b_ind][0]+=1
                            print('hi26')
                            star_indices[b_ind][1] += 1 #store the next index to check in case we get to 2
                            b_ind += 1 # set my index to next b 
                            s_ind += 1 # set my index to next s
                                                        
                            continue                                        
                        #first star fails
                        else:
                            if highest_active == 0:
                                print('hi27')
                                return False
                            #set the star back to 0 count
                            else:
                                print('hi72')
                                star_indices[b_ind][0] = -1
                                highest_active -=1
                                highest_ind = index_list[highest_active]
                                continue
                continue

        else:

            #letters match, first star or not last b or not last s
            if let_check(b[b_ind],s[s_ind]) and (b_ind != len(b)-1 or s_ind == len(s)-1 or highest_active == -1):        
                print('hi45')
                b_ind += 1
                s_ind += 1
                continue
            
            
            #letters don't match or not first star or last b or last s   
            
            else: #need to check for active stars and either iterate or fall back to highest one
                print('hi50')                

                while 1==1 : #loop will run until manual break                   

                    if highest_active == -1: #no stars active
                        print('hi12')
                        return False

                    #check our current active star

                    elif star_indices[highest_ind][0] == 0: #current count 0
                        print('hi13', b[b_ind], s[s_ind],highest_ind)                                             
                        star_indices[highest_ind][0] = 1 #set to 1 and check
                        d = highest_ind
                        e = star_indices[highest_ind][1]           

                        if let_check(b[d], s[e]):
                            print('hi14')
                            b_ind = d + 1 # set my index to next b 
                            s_ind = e + 1 # set my index to next s
                            star_indices[highest_ind][1] = s_ind #store the next index to check in case we get to 2                            
                            break
                        #current count 0 but letters don't match
                        else:
                            print('hi15')
                            if highest_active == 0: #first star has failed 0 and 1
                                return False
                            #not the first star active
                            else:
                                print('hi16')
                                star_indices[highest_ind][0]=-1                                                             
                                highest_active -= 1 #need to check last active
                                highest_ind = index_list[highest_active]                                
                                continue
                    #our current star is on a successful 1 or more count
                    elif star_indices[highest_ind][0] >= 1:# increase by 1 and try
                        print('hi17')
                        star_indices[highest_ind][0]+=1
                        d = highest_ind
                        e = star_indices[highest_ind][1]                                                
                        #next count passes, move up count and index
                        if let_check(b[d], s[e]): #check the increased by 1
                            print('hi18')
                            b_ind = d + 1 # set my index to next b 
                            s_ind = e + 1 # set my index to next s
                            star_indices[highest_ind][1] = e+1 #store the next index to check in case we get to 2                            
                            break                                         
                        #next count fails
                        else:
                            if highest_active == 0:
                                print('hi19')
                                return False
                            #drop the highest active
                            else:
                                print('hi55')
                                highest_active -=1
                                highest_ind = index_list[highest_active]
                                star_indices[highest_ind][0]=-1
                                continue




    if s_ind == len(s) and b_ind == len(b):
        return True

    elif s_ind == len(s):

        for y in range((b_ind),len(b)):
            print('hi31',y)
            if y in star_indices.keys():# we reached the end of s and the rest of b is *s
                print('hi30')
                continue
            else:
                return False
        else:
            return True

    else:
        print('hi9')
        return False


x = "cabbbbcbcacbabc"
y = ".*b.*.ab*.*b*a*c"


print(string_comp(x,y))
