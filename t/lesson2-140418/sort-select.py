# Straight Selection Sort

arr = [45,38,65,97,76,13,27,49]
print arr
print "==========================="
for i in range(len(arr)):
    min_value = arr[i]
    min_index = i
    for j in range(i+1,len(arr)):
        if arr[j] < min_value:
            min_value = arr[j]
            min_index = j
    arr[i],arr[min_index] = arr[min_index],arr[i]
    print arr
print "==========================="
print arr
 
    
    
