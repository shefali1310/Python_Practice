N = int(raw_input("Enter a number:"))
if N%3 == 0 and N%5 == 0:
    print "Fizz Buzz"
elif N%3 == 0:
    print "Fizz"
elif N%5 == 0:
    print "Buzz"