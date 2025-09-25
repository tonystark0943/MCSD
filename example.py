# a = 19
# b = 10
# print(a, b)
# a,b = b,a
# print(a, b)

# str = '''Hello
# Peter'''
# print(str)

# print(3*1**3)
# print(8/2*4)

# x = 10
# y = int('20')
# print(x + y)

# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print(f"You are not eligible to vote. You need {18 - age} more years.")

# s = input("Enter a string: ")

# for char in s:
#     if char in 'aeiouAEIOU':
#         continue
#     else:
#         print(char, end="")

def calc(a,b):
    return a+b, a-b, a*b, a/b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(calc(x, y))
    