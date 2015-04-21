flag = "num"
sum = 0
while flag == "num":
    x = raw_input("Please input num: ")
    if x == "pc":
	flag = "str"
    else:
        sum += int(x)
print "sum is %s " % sum
    
