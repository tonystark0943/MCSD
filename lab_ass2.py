# Lab Assignment 2
# Name: Pratik Ranjan Mahala
# Regd No: 24E113A07
# Serial No: 15

#1
str = input("Enter a string: ")
idx = -len(str)
for i in range(len(str)):
    print(f"The character present at positive index {i} and negative index {idx} is {str[i]}")
    idx+=1

#2a
s = input("Enter a string: ")
print(f"Original String: {s}")
print(f"Strip: {s.strip("e")}")
print(f"Length: {len(s)}")
print(f"Right Strip: {s.rstrip("er")}")
print(f"Left Strip: {s.lstrip("He")}")
print(f"Find: {s.find("l")}")
print(f"RFind: {s.rfind("l")}")
print(f"Index: {s.index("l")}")
print(f"RIndex: {s.rindex("l")}")
print(f"Count: {s.count("l")}")
print(f"Replace: {s.replace("l", "p")}")
print(f"Split: {s.split("e")}")
print(f"Join: {"_".join(s)}")
print(f"Uppercase: {s.upper()}")
print(f"Lowercase: {s.lower()}")
print(f"Swapcase: {s.swapcase()}")
print(f"Titlecase: {s.title()}")
print(f"Capitalize: {s.capitalize()}")
print(f"Startswith: {s.startswith("He")}")
print(f"Endswith: {s.endswith("lo")}")

#3
str = input("Enter a string: ")
i = len(str)-1
while i>=0:
    print(str[i], end="")
    i-=1

#4
s = input("Enter a string: ")
for ch in s:
    print(chr(ord(ch)+3), end="")

#5b
def removeDuplicates(lst):
    for i in range(len(lst)-1, -1, -1):
        if lst.count(lst[i]) > 1:
            lst.remove(lst[i])
    return lst

lst = [26, 13, 56, 26, 78, 13, 90, 13, 56, 100, 78, 56]
print(removeDuplicates(lst))

#6
n = int(input("Enter list size: "))
lst = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    lst.append(num)
print("Original List:", lst)
print("Maximum:", max(lst))

#7
n = int(input("Enter list size: "))
lst = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    lst.append(num)
print("Original List:", lst)
print("Sum:", sum(lst))
print("Average:", sum(lst)/len(lst))
