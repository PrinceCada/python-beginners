#Loop in python
#While Loop (also known as indefinite or conditional loop)

#Example 1
count = 0
while count<9:
    print("Number:", count)
    count+=1
print("Goodbye!")


#Example 2
#Guess game using while loop
import random
n = 20
to_be_guessed = int(n * random.random()) +1
guess = 0


while guess != to_be_guessed:
    while True:                                 #This condition is for allowing integer only
        try:
            guess = int(input("New number: "))
            break
        except:
            print("Integer is only allowed!")
    if guess > 0:
        if guess > to_be_guessed:
            print("The number is too large")
        elif guess < to_be_guessed:
            print("The number is too small")
    else:
        print("Sorry that you're giving up!")
        break
else:
    print("Congratulation for guessing the correct number")
#End of while loop







