num_1 = int(raw_input("Enter your first number: "))
num_2 = int(raw_input("Enter your second number: "))
operator = raw_input("Enter the arithmetic operator you wish to perform on your entered numbers: ")
if operator == "+" :
    print num_1 + num_2
elif operator == "-" :
    if num_1>num_2 :
        print num_1 - num_2
    else:
        print num_2 - num_1
elif operator == "/" :
    print num_1 / num_2
elif operator == "*" :
    print num_1 * num_2
elif operator == "%" :
    print num_1 % num_2
