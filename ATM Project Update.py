import datetime
import random

database = {}  # dictionary


def init():
    print("Welcome to BankPython, what would you like to do?")
    print("1. Login")
    print("2. Register")

    haveAccount = int(input())

    if (haveAccount == 1):

        login()
    elif (haveAccount == 2):

        register()
    else:
        print("You have selected invalid option")
        init()


def login():
    print("********* Login ***********")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber, userDetails in database.items():
        if accountNumber == accountNumberFromUser:
            if userDetails[3] == password:
                Date = datetime.datetime.now()
                print(Date)
                bankOperation(userDetails)
    else:
        print('Invalid account or password, Please try again')
        login()


def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()


def bankOperation(userDetails):
    print("Welcome %s %s " % (userDetails[1], userDetails[0]))

    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Complain (4) Logout (5) "
                               "Exit \n"))

    if (selectedOption == 1):

        depositOperation()
    elif (selectedOption == 2):

        withdrawalOperation()
    elif (selectedOption == 3):

        complain()
    elif (selectedOption == 4):

        logout()
    elif (selectedOption == 5):

        exit()
    else:
        print("Invalid option selected")
        bankOperation(userDetails)


def withdrawalOperation():
    print("withdrawal")
    withdraw = input('How much would you like to withdraw \n')
    print('Take your cash %s' % withdraw)
    exit()


def depositOperation():
    print("Deposit Operations")
    deposit = input('How much would you like to deposit \n')
    print('Your current balance is %s' % deposit)
    exit()


def complain():
    complaint = input('What issue will you like to report? \n')
    print('Thank you for contacting us!')
    exit()


def generationAccountNumber():
    return random.randrange(1111111111, 9999999999)


def logout():
    init()


init()
