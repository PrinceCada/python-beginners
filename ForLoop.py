#Loop in python
#For Loop (repeats a group of statements a specified number or times)

#Example 1
fruits = ['Grapes', 'Banana', 'Apple', 'Oranges']

for fruits in fruits:
    print("Current fruit:", fruits)
print("Goodbye!")


#Example 2
#Factorial

while True:
    try:
        num = int(input("Number:"))
        break
    except:
        print("Integer are only allowed!")

factorial = 1

if num < 0:
    print("Number must be positive")
elif num == 0:
    print("factorial = 1")
else:
    for i in range(1,num + 1):
        factorial = factorial * i
print(factorial)