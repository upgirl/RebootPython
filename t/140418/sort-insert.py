# Straight Insertion Sort
#arr = [4,4,3,1,2]
arr = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
print arr

for i in range(1,len(arr)):
    #print "==== index" + str(i) + ":waitInsert=" + str(arr[i])
    for j in range(i):
        k = i-j
        if arr[k] < arr[k-1]:
            arr[k],arr[k-1] = arr[k-1],arr[k]
        #print k,k-1,arr
print arr
