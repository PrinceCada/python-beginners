#Hourglass Pattern
def pattern(n):
    k = n - 2
    for i in range(n, -1, -1):  # This loop is for our outer rows
        for j in range(k, 0, -1):  # This loop is for column
            print(end=" ")
        k = k + 1
        for u in range(0, i + 1):  # I do this loops because it is moving forward
            print("* ", end="")
        print("\r")
    k = 2 * n - 2
    for i in range(0, n+1):  # This loop is for our outer rows
        for j in range(0, k):  # This loop is for column
            print(end=" ")
        k = k - 1
        for u in range(0, i + 1):  # I do this loops because it is moving forward
            print("* ", end="")
        print("\r")

pattern(5)