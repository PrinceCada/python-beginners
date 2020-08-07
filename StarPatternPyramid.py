#Star Pattern Pyramid
def pattern(n):
    k = 2  * n - 2                  #You can play with this, purpose is location or position only
    for i in range(0,n):            #This loop is for our outer rows
        for j in range(0,k):        #This loop is for column
            print(end = " ")
        k = k - 1
        for u in range(0, i + 1):   #I do this loops because it is moving forward
            print("* ",end="")
        print("\r")
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
