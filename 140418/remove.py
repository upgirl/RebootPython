arr = ['a','a','b','c']
s = 'aa'

# remove
#for c in range(arr.count(s)):
#	arr.remove(s)
#print arr
#exit()

for c in range(arr.count(s)):
    i = arr.index(s)
    del arr[i]
print arr


