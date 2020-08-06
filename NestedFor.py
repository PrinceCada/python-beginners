#Three integers satisfying a^2 + b^2 = c^2 are called pythagorean numbers
from math import sqrt                #Import square root from math
n = int(input("Max number "))        #This will serve as your max number for loop
for a in range (1,n+1):              #First loop will loop range from (1 to n number or max number you input)
    for b in range (a,n):
        c_square = a**2 + b**2       #This is same as a square + b square
        c = int(sqrt(c_square))
        if ((c_square - c**2) == 0): #If the condition meet it will print the 'a b c'
            print(a,b,c)


#Sample Output
#Max number 20
#3 4 5
#5 12 13
#6 8 10
#8 15 17
#9 12 15
#12 16 20
