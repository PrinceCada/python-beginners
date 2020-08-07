#Right Alphabetical Pattern
def pattern(n):
    k = 2 * n - 2                       #Position only, you can play with here.
    x = 65
    for i in  range(0,n):
        ch = chr(x)
        x += 1                          #It is equal also as " x = x + 1" (Increment)
        for j in range(0, i+1):
            print(ch, end=" ")
        print("\r")

pattern(10)


#Output
A 
B B 
C C C 
D D D D 
E E E E E 
F F F F F F 
G G G G G G G 
H H H H H H H H 
I I I I I I I I I 
J J J J J J J J J J 
