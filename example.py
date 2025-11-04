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

# def calc(a,b):
#     return a+b, a-b, a*b, a/b

# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# print(calc(x, y))

# mem = [0]*8
# mem[3] = 4
# mem[5] = 9
# sum = mem[3] + mem[5]
# mem[6] = sum
# mem[7] = mem[5] - mem[3]

# print("mem[3]:", mem[3])
# print("mem[6]:", mem[6])
# print("mem[7]:", mem[7])
# print("Memory: ", mem)

# mem = [7,5,4,0,3,9,0,0]
# pointer0 = mem[0]
# pointer1 = mem[1]
# pointer2 = mem[2]
# source1 = mem[pointer1]
# source2 = mem[pointer2]
# result = source1 + source2
# mem[pointer0] = result
# print("Memory:", mem)

# memory = [0]*10

# def read(address):
#     if 0<=address<len(memory):
#         print(f"READ: Value at address {address} = {memory[address]}")
#     else:
#         print("Invalid memory address")

# def write(address, value):
#     if 0<=address<len(memory):
#         memory[address] = value
#         print(f"WRITE: Stored {value} at address {address}")
#     else:
#         print("Invalid memory address")

# read(3)
# write(3, 15)

stack=[0]*5
TOP=-1

def push(value):
    global TOP
    if TOP < len(stack)-1:
        TOP += 1
        stack[TOP] = value
        print(f"{value} pushed to stack")
    else:
        print("Stack Overflow")

def pop():
    global TOP
    if TOP >= 0:
        value = stack[TOP]
        TOP -= 1
        print(f"{value} popped from stack")
        return value
    else:
        print("Stack Underflow")
        return None

def peek():
    if TOP >= 0:
        return stack[TOP]
    else:
        print("Stack is empty")
        return None

push(10)
push(20)
pop()
push(30)
pop()
print("Top element is:", peek())
 