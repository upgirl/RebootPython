passwd = 'redhat'
shoplist = ['books','pens','cups','warter']

errcount = 0
while errcount<3:
    pwd = raw_input("Please input password: ")
    if pwd != passwd:
        errcount += 1
    else:
        print "Welcome shopping ..."
        print shoplist
        buylist = []
        while True:
             x = raw_input("Select which good? ")
             if x and x in shoplist:
                 buylist.append(x) 
             else:
                 print buylist
        break

