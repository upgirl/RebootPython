# Straight Insertion Sort
arr = [4,3,1,2]
print arr

for i in range(1,len(arr)):
    #print "==== index" + str(i) + ":waitInsert=" + str(arr[i])
    for j in range(i):
        k = i-j
        if arr[k] < arr[k-1]:
            arr[k],arr[k-1] = arr[k-1],arr[k]
        #print k,k-1,arr
print arr
