#Nested Loop

#Example 1
#Note ( '\n' = stands for Newline)

print("Welcome to PRINCE Bank ATM\n")
restart = 'y'
balance = 100.00
chances = 3

while chances >= 0:
    pin = int(input("Please enter your PIN: "))
    if pin == 1234:
        print("You entered your pin correctly\n")
        while restart not in ('n','NO','no','N'):
            print("Press 1 for your Balance\n")
            print("Press 2 for your Withdraw\n")
            print("Press 3 for your Cash in\n")
            print("Press 4 for your Return Card\n")
            option = int(input("What would you like to choose? "))

            if option == 1:                          #This is for option 1 which is Balance inquiry
                print("Your Balance: ", balance)
                restart = input("Would you like to go back? y/n: ")
                if restart in ('n','NO','no','N'):   #This is execute when you choose value 'n'
                    print("Thank you!")
                    break
            elif option == 2:                        #This is for option 2 which is Withdraw
                option2 = 'Y'
                withdraw = float(input("How much you want to withdraw?\n" + "10/20/30/40/50/60/70/80/90/100/200/300/400/500: "))
                if withdraw in [10,20,30,40,50,60,70,80,90,100,200,300,400,500,1000]:
                    balance = balance - withdraw
                    print("\nYour balance now is : ", balance)
                    restart = input("Would you like to go back? y/n: ")
                    if restart in ('n', 'NO', 'no', 'N'):
                        print("Thank you!")
                        break
                elif withdraw not in [10,20,30,40,50,60,70,80,90,100,200,300,400,500,1000]:   #This condition is for not choosing within the list
                    print("Invalid amount, Please retry\n")
                    restart = 'Y'
                elif withdraw == 1:
                    withdraw = float(input("Please enter the desired amount!"))

            elif option == 3:
                Pay_in = float(input("How much you want to cash in? "))
                balance = balance + Pay_in
                print("\nYour balance now is: ", balance)
                restart = input("Would you like to go back? y/n: ")
                if restart in ('n', 'NO', 'no', 'N'):
                    print("Thank you!")
                    break

            elif option == 4:
                print("Please wait while your card is Returned\n")
                print("Thank you for your service!")
                break

        else:
            print("Enter the correct number \n")
            restart = 'Y'

    elif pin != 1234:
        print("Your pin is incorrect, Please Try Again\n")
        chances -=1                     #This is same as chances = chances - 1

        if chances == 0:
            print("\n No more tries")
            break





