year = raw_input("enter the year to check whether its leap year or not:")
if int(year)%4 == 0:
    if int(year)%100 != 100 and int(year)%400 == 0:
        print "the year is a leap year"
    else:
        print "the year is not a leap year"
else:
    print "the year is not a leap year"