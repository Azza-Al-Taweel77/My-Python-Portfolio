names= input("Enter the first name and last name of your friends separated by a comma: ").split(", ")
name_parts=[]

for name in names:
    new_name= name.split()
    print(new_name)

    first_name= new_name[0]
    last_name= new_name[1]

    first_initial= first_name[0]
    last_initial= last_name[0]

    abbreviated= first_initial + "." + last_initial + "."

    name_parts.append(abbreviated)
print("Abbreviated Names: ")
for M in name_parts:
    print(M)