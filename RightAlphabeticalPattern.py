#Right Alphabetical Pattern
def pattern(n):
    k = 2 * n - 2
    x = 65
    for i in  range(0,n):
        ch = chr(x)
        x += 1
        for j in range(0, i+1):
            print(ch, end=" ")
        print("\r")

pattern(10)