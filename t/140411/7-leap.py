flag = "noleap"
while flag == "noleap":
    year = int(raw_input("Please input year: "))
    if year%400==0 or (year%100!=0 and year%4==0):
        flag = "leap"
        print "Good! %s is leap year " % year
    else:
        print "Sorry! %s is noleap year " % year

