errcount = 0
while errcount<3:
    pwd = raw_input("Please input password: ")
    if pwd != 'redhat':
        errcount += 1
    else:
        print "Welcome"
        break
    
            
