sum = 0
loop = 0
while True:
    x = raw_input('Please input num: ')
    if not x:
        break
    loop += 1.0
    sum += int(x)
print "avg is %s " % (sum/loop)
