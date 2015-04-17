nlist = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max1 = nlist[0]
max2 = nlist[0]
tmp = 0
for n in nlist:
    if n > max1:
        tmp = max1
        max1 = n
        if tmp > max2:
            max2 = tmp
    elif n > max2:
        max2 = n
print "max1=%s ,max2=%s" % (max1,max2)



