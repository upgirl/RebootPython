nlist = [65555,1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,45,33,45,65535]

# init max_one and max_two
max_one = nlist[0]
max_two = nlist[1]
if max_two > max_one:
    max_one = nlist[1]
    max_two = nlist[0]
print max_one,max_two

# yi ci hou tui
for n in nlist:
    if n > max_one:
        max_two = max_one
        max_one = n
    elif max_one > n > max_two:
        max_two = n
    #print max_one,max_two
# print result        
print max_one,max_two
        



