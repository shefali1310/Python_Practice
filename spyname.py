first_name = raw_input("first name")
last_name = raw_input("last name")
gender = raw_input("gender")
number = raw_input("number")
email_id = raw_input("email id")
amount_paid = raw_input("amount paid")

print  "To" + email_id
print 'mobile:' + number
if gender == "Male" or gender == "male":
        print "Hi, " + "Mr." + first_name + "" + last_name
else:
        print "Hi, " + "Miss " + first_name + "" + last_name
r=0 #remaining value
v=2499#amount to be paid
if amount_paid == 2499:
    r = (v - int(amount_paid))
    print "Welcome to the Acadview internship program! We have successfully received the payment of " , v , "."
else:
    r = (v - int(amount_paid))
    print "Welcome to the Acadview internship program! We have successfully received the payment of " , amount_paid , ". " ,  "You need to pay:" , r

