arr = [1,2,3,3,4,2]
print arr

arr_new = []
for i in arr:
    if i not in arr_new:
        arr_new.append(i)     
arr = arr_new
print arr

