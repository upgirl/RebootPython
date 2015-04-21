# extend

# extend, change 
arr_one = [1,2,3,4]
arr_two = [5,6,7,8]
arr_one.extend(arr_two)
print arr_one

#1 add, no change, set
arr_one = [1,2,3,4]
arr_two = [5,6,7,8]
arr_one =  arr_one + arr_two
print arr_one

#2 recurse arr_two ,append to arr_one
arr_one = [1,2,3,4]
arr_two = [5,6,7,8]
for n in arr_two:
    arr_one.append(n)
print arr_one


