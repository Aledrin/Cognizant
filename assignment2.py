#TASK 1
n= int(input("Give me a number: "))
print("Your number is",n)

while n>0:
    n-1
    print (n, end=" ")
    n-=1
print ("Blast off!")

#TASK 2
print("Multiplication table")
n2= int(input("Give me a number again: "))
print("Your number is",n2)
m=0
for i in range(11):
    
    print(n2,"*",m,"=",n2*m)
    m+=1
#TASK 3
print("Lets find the factorial")
n3= int(input("Give me a number again: "))
print("Your number is",n3)
if n3<0:
     print("No factorial for negative numbers")
else:
     factorial=1
for i in range(1, n3 + 1):
        factorial *= i  
print("Your factorial is",factorial)

    
    