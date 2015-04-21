arr = [4,4,3,4,2]
s = 4

print arr.index(s,arr.index(s)+1)

i = 0
c = 0
for n in arr:
    if n == s:
        c += 1
        if c == 2:
            break
    i += 1
print i 

print "================="
i = -1
for n in range(arr.count(s)):
    i = arr.index(s,i+1)
    print i
