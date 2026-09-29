i=1
evencount=0
oddcount=0
evensum=0
oddsum=0
totalsum=0
while(i<=5):
    n=int(input("Enter Number:"))
    if(n%2==0):
        print(n,"is Even")
        #evencount variable count number of times even number is input
        evencount=evencount+1
        #evensum variable counts the total value of even numbers entered by user
        evensum=evensum+n
    else:
        print(n,"is Odd")
        #oddcount variable count number of times odd number is input
        oddcount=oddcount+1
        #oddsum variable counts the total value of odd numbers entered by user
        oddsum=oddsum+n
    #totalsum varaible counts the total value of all values entered by user
    totalsum=totalsum+n
    i=i+1
print("Even count is",evencount)
print("Odd count is",oddcount)
print("Even sum is",evensum)
print("Odd sum is",oddsum)
print("Total sum is",totalsum)