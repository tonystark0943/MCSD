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

#8
numbers = []

print("Enter 10 integers:")
for i in range(1, 11):
    num = int(input(f"Enter integer {i}: "))
    numbers.append(num)

search_num = int(input("Enter the number to search for: "))

count = numbers.count(search_num)

if count > 0:
    print(f"The number {search_num} is present in the list and appears {count} time(s).")
else:
    print(f"The number {search_num} is not present in the list.")

#9
import random

matrix = [[random.randint(0, 1) for _ in range(4)] for _ in range(4)]

for row in matrix:
    print(''.join(str(num) for num in row))

max_row_index = max(range(4), key=lambda i: sum(matrix[i]))
max_col_index = max(range(4), key=lambda j: sum(matrix[i][j] for i in range(4)))

print(f"The largest row index: {max_row_index}")
print(f"The largest column index: {max_col_index}")


#10
students = {}

num = int(input("Enter number of students: "))
for _ in range(num):
    name = input("Enter Student Name: ")
    marks = float(input("Enter % of Marks of Student: "))
    students[name] = marks

print("Name of Student")
for name in students:
    print(name)

print("% of Marks")
for name in students:
    print(students[name])

#11
students = {}

num = int(input("Enter the number of students: "))
for _ in range(num):
    name = input("Enter Student Name: ")
    marks = int(input("Enter Student Marks: "))
    students[name] = marks

while True:
    search_name = input("Enter Student Name to get Marks: ")
    if search_name in students:
        print(f"The Marks of {search_name} are {students[search_name]}")
    else:
        print(f"No record found for student named {search_name}")
    
    choice = input("Do you want to find another student marks[Yes|No] ")
    if choice.lower() != "yes":
        break
    
#12
data = input("Enter the data into a file : ")

with open("sample.txt", "w") as file:
    file.write(data)

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

#13
n = int(input("Enter the first n number to reverse in a file : "))

with open("data.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    reversed_part = line[:n][::-1]
    remaining_part = line[n:]
    print(reversed_part + remaining_part)

#14
import string

filename = "ex1.txt"
word_count = 0

with open(filename, "r") as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            cleaned = word.strip(string.punctuation).lower()
            if cleaned:
                print(cleaned)
                word_count += 1

print(f"{filename} has {word_count} 'words'")

#15
filename = input("Enter a file name : ")

with open(filename, "r") as file:
    lines = file.readlines()

print(lines)

num_chars = sum(len(line) for line in lines)
num_words = sum(len(line.split()) for line in lines)
num_lines = len(lines)

print(f"The number of Characters are : {num_chars}")
print(f"The number of Words are : {num_words}")
print(f"The number of Lines are : {num_lines}")