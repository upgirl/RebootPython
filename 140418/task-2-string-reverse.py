string = 'hello'
arr = list(string)
arr.reverse()
s = ''
for i in arr:
    s += i
print "origin string is: %s" % string
print "after reverse is: %s" % s
