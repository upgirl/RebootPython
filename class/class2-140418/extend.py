arr_one = [1,2,3,4]
arr_two = [5,6,7,8,4]

# add, no change
arr_one =  arr_one + arr_two
print arr_one
print arr_two

# extend, change 
arr_one.extend(arr_two)
print arr_one
print arr_two

# append
#a.append(b)
#print a
