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


#Output
1  
1  1  
1  1  1  
1  2  2  1  
1  3  4  3  1  
1  4  8  8  4  1  
1  5  12  20  12  5  1  
1  6  18  36  36  18  6  1  
1  7  24  56  98  56  24  7  1  
1  8  32  85  170  170  85  32  8  1 
