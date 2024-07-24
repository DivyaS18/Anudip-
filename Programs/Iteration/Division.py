#to display the numbers between 10 to 500 divisible by 10 and 7
for x in range(10,500):
    if(x%7==0 and x % 10 == 0):
        print(x)


#count the numbers between 100 to 1000 which is even and divisible by 3 using for loop
print("The numbers between 100 to 1000 which is even and divisible by 3\n")
count=0
for x in range(100,1000,2):
    if(x%3==0):
        count+=1
        print(x, end=" ")
        
print("\nCount is:",count)

#display total number between 100 to 1000 which is even asnd divisible by 3 using while loop
print("\nThe numbers between 100 to 1000 which is even and divisible by 3\n")
x=100
c=0
while(x < 1000):
    if(x%2 == 0 and x%3 == 0):
        print(x, end=" ")
        c+=1
    x=x+1
print("\ncount is:", c)
        
