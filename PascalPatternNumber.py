#Pascal Pattern
def pattern(n):
    for i in range(0,n):                            #Outer rows
        for j in range(0, i + 1):                   #columns
            print(function(i,j), " ", end="")
        print()
def function(n,k):
    res = 1
    #Pascal logic pattern
    if k > n - k:
        k = n - k
    for i in range(0,k):
        res = res * (n - 1)
        res = res // (i + 1)    #Floor division
    return res

pattern(10)