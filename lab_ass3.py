#1
memory = [1, 2, 3, 4, 5]

for i in range(len(memory)):
    print(f"Address {i}: {memory[i]}")

#2
memory = []
def create():
    size = int(input("Enter size of memory to create: "))
    global memory
    memory = [0] * size
    print(f"Memory of size {size} created.")

def read():
    global memory
    for i in range(len(memory)):
        print(f"Address {i}: {memory[i]}")

def write():
    global memory
    address = int(input("Enter address: "))
    value = int(input("Enter value: "))
    if 0 <= address < len(memory):
        memory[address] = value
        print(f"Value {value} written at address {address}.")
    else:
        print("Invalid address.")

while True:
    print("MENU")
    print("1. CREATE")
    print("2. READ")
    print("3. WRITE")

    choice = input("Enter your choice (1-3) or 'Q' to quit: ")

    if choice.upper() == 'Q':
        break
    elif choice == '1':
        create()
    elif choice == '2':
        read()
    elif choice == '3':
        write()
    else:
        print("Invalid choice. Please try again.")

#3
