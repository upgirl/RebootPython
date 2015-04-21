arr1 = [1,2,3,3,4,2]
arr2 = [1,5,3,3,6,2]

arr_new = []
for i in arr1:
    if i in arr2 and i not in arr_new:
            arr_new.append(i)
print arr_new

print arr1
print arr2
