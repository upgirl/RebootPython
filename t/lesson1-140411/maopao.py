nlist = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
ndic = {}
len = 0
# Remove repeat and number them in order
for n in nlist:
    if str(n) not in ndic:
        ndic[str(n)] = len
        len += 1
# Sort max >>>> min 
for i in range(len):
    for j in range(i+1,len):
        a = ""
        b = ""
        for k in ndic:
            if ndic[k] == i:
                a = k
            if ndic[k] == j:
                b = k
        if int(a) < int(b):
            ndic[a] = j
            ndic[b] = i
# Top 2
print "== Top 2 =="
for i in range(2):
    for k in ndic:
        if ndic[k] == i:
            print k

