#n=5
"""     *
       * *
      * * *
     * * * *
    * * * * *
"""
for i in range(5):
    for j in range(i,4):
        
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    
   # n=n-1
    print()
"""for i in range(4):
    for j in range(i+1):
        
        print(" ",end=" ")
    for j in range(i,3):
        print("*",end=" ")
    for j in range(i,4):
        print("*",end=" ")
   # n=n-1
    print()"""