#Task 1
a="Python is amazing!"
print("First word:",a[0:6])
print("Amazing part:",a[10:17])
print("Reversed String:",a[::-1])
#Task 2
b="hello, python world!"
stripb=b.strip()
print("After strip():", stripb)
capb=b.capitalize()
print("After capitalize():", capb)
repb=b.replace("world", "universe")
print("After replace():", repb)
upb=b.upper()
print("After upper():", upb)

#Task 3
n= input("Give me a word: ")
print("Your word is:",n)
rev=n[::-1]
if n==rev:
    print("You have a palindrome")
else:
    print("This is not a palindrome")