arr = []

# stack

# in 1 2 3
print "1 in"
arr.append(1) 
print "2 in"
arr.append(2) 
print "3 in"
arr.append(3) 
print arr

# out 3 2 1
for i in range(len(arr)):
    print "%s out" % arr.pop()
print arr
