#Task 1
fruit=["apple", "orange", "banana", "coco", "cherry"]
print("elements in the list: ",len(fruit))
print("Original list: ",fruit)
fruit.append("strawberry")
print("After adding a fruit: ",fruit)
fruit.remove("apple")
print("After removing a fruit: ",fruit)
fruit[0] = "pineapple"
print("After change a fruit: ",fruit)
print("reversed list: ",fruit[::-1])
#Task 2
info = {"name": "David", "age": 23, "city": "Phoenix"}
print("original:",info)
info["favorite color"] = "Red"
info["city"] = "Guadalajara"
print("modified:",info)

del info["age"]
for key, value in info.items():
    print(f"{key}: {value}")

#Task 3
tup = (1, 2, 3)
print(tup)
try:
    tup[0] = "4"
except TypeError as e:
    print(f"Error: {e}")

print(f"Length of the tuple: {len(tup)}")
