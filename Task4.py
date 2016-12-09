print "[======================]"
print "  1. Returning Customer"
print "  2. New Customer"
print "  3. Guest"
print "[======================]\n"
option = 0


def new():
    try:
        customer_file = open('CustomerList.txt', 'r+')
        customer_lists = list(customer_file)
        file_index = len(customer_lists)
        customer_file.close()
        print "Thank you for creating an account."
        print "First, we need to ask a few questions"
        print '\n'
        customer_first = raw_input("What is your first name? \n").title()
        customer_last = raw_input("What is your last name? \n").title()
        customer_address = raw_input("What is your street address? \n").title()
        customer_city = raw_input("What city do you live in? \n").title()
        customer_state = raw_input("What state do you live in? \n").upper()
        customer_zip = raw_input("What is your zipcode?\n")
        customer_phone = raw_input("What is your phone number? \n")
        phone_con = str(file_index+1) + customer_phone[6:]
        new_customer = phone_con + ", " + customer_first + ", " + customer_last + ", " + customer_address + ", " + customer_city + ", " + customer_state + ", " + customer_zip + ", " + customer_phone + "\n"
        verify_info = ("\n" + customer_first + " " + customer_last + "\n" + customer_address + "\n" + customer_city + ", " + customer_state + "  " + customer_zip + "\n" + customer_phone + "\n")
        print verify_info
        verify()
        print "\n" + customer_first + " your customer number is " + phone_con
        customer_file = open('CustomerList.txt', 'a+')
        customer_file.write(new_customer)
        customer_file.close()
    except IOError:
        print "Something went wrong"


def verify():
    verified = raw_input("Is the information you entered correct?\n Y/N\n").upper()
    if verified == 'N':
        print "\nLet's try again.\n"
        new()
    else:
        print "Thank you"


def get_customer():
    customer_id = raw_input('Please enter your user ID: \n')
    print '\n'
    return customer_id


def find_customer(customer_id):
    try:
        with open('CustomerList.txt', 'r+') as lists:
            customer_list = lists.readlines()
            for line in customer_list:
                record = line.split(',')
                if customer_id == record[0]:
                    return record
        return 'none'

    except IOError:
        print ("File not found")


def confirm():
    confirmation = raw_input("Is this the correct informaton?: \nY/N\n").capitalize()

    if confirmation == 'N':
        print "Please re-submit the correct information. \n"
        returning()

    else:
        print 'Thank you'


def returning():
    customer = get_customer()
    records = find_customer(customer)
    if records == 'none':
        print "Customer ID not found"
        returning()

    else:
        for items in records:
            print items

        confirm()
    return


def guest():
    print "Hello, thank you for shopping with us today. How may I be of service to you? \n"


def error():
    print ValueError('Please select 1 for Returning Customer, 2 for New Customer, or 3 for Guest')

while option < 1 or option > 3:
    try:
        option = (int(raw_input("Please select your customer type\n Enter a number between 1 and 3: \n")))
    except ValueError:
        print 'Selection must be number \n'
    if option == 1:
        returning()
    elif option == 2:
        new()
    elif option == 3:
        guest()
    else:
        error()
