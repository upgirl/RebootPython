# Straight Insertion Sort
arr = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
print arr
for i in range(1,len(arr)):
    tmp = arr[i]
    j = i - 1
    while (j > -1 and tmp < arr[j]):
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = tmp
    #print i,tmp,arr
print arr

print '========================================'

arr = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
print arr
for i in range(1,len(arr)):
    for j in range(i):
        k = i-j
        if arr[k] < arr[k-1]:
            arr[k],arr[k-1] = arr[k-1],arr[k]
        #print k,k-1,arr
print arr


