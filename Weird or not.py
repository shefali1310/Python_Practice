n = int(raw_input())
if n % 2 != 0:
    print "Weird"

elif n % 2 == 0 and n in range(1, 6):
    print "Not Weird"

elif n % 2 == 0 and n in range(5, 21):
    print "Weird"

elif n % 2 == 0 and n > 20:
    print "Not Weird"