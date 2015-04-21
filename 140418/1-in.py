# dic search fast than list
# function: in

demo_list = [1,2,'a','b']
s = 11

print s in demo_list

# 
is_inlist = False
for demo in demo_list:
    if demo == s:
        is_inlist = True  
        break
print is_inlist

