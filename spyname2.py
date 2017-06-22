first_name = raw_input("first name")
last_name = raw_input("last name")
salutation = raw_input("What should we call you Mr. or Miss?")
number = raw_input("number")
email_id = raw_input("email id")
amount_paid = raw_input("amount paid")

print  "To" + email_id
print 'mobile:' + number
print 'Hi, ' + salutation + ' ' + first_name + "" + last_name
r=0 #remaining value
v=2499#amount to be paid
r = v - int(amount_paid)
print 'Welcome to the acadview Internship program! We have successfully received the payment of Rs.' , amount_paid , '. You need to pay' , r , ' more.'

