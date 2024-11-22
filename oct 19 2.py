first_name = input("entre your first name:")
last_name = input("entre your last name:")
name = first_name+" "+last_name
print(name)
last_name_length=len(first_name)
print(last_name_length)
extracted_last_name=name[last_name_length+1:]
print(extracted_last_name)

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()
