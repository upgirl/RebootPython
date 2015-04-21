arr = [1,77,65555,33,45]
print arr
print "=========================="
# min << max
#for i in range(len(arr)):
#    for j in range(i+1,len(arr)):
#        if arr[j] < arr[i]:
            #tmp = arr[j]
            #arr[j] = arr[i]
            #arr[i] = tmp
            #arr[i],arr[j] = arr[j],arr[i]
#            arr[j],arr[i] = arr[i],arr[j]
#print arr 

# maopao
for j in range(len(arr)):
    #for i in range(len(arr)-1):
    for i in range(len(arr)-1-j):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
    print arr
print "==================="
#
arr = [1,77,65555,33,45]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j] < arr[i]:
            arr[i],arr[j] = arr[j],arr[i]
    print arr

print arr 
