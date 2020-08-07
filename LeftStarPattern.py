#Left Star Pattern
def pattern(n):
    k = 2 * n - 2                   #Position
    for i in range(0, n -1):        #Outer rows
        for j in range(0,k):        #for column
            print(end=" ")
        k = k - 2                   #Decrement
        for j in range (0, i +1):
            print("* ", end="")
        print("\n")
    k = - 1
    for i in range (n-1,-1,-1):
        for j in range (k, -1, -1):
            print(end=" ")
        k = k + 2
        for j in range (0, i + 1):
            print("* ", end="")
        print("\n")

pattern(10)


#Output
                  * 
                * * 
              * * * 
            * * * * 
          * * * * * 
        * * * * * * 
      * * * * * * * 
    * * * * * * * * 
  * * * * * * * * * 
* * * * * * * * * * 
  * * * * * * * * * 
    * * * * * * * * 
      * * * * * * * 
        * * * * * * 
          * * * * * 
            * * * * 
              * * * 
                * * 
                  * 
