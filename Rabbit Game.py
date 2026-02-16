print("Welcome to place the rabbit")
place= [["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"]]
print(f"{place[0]} \n{place[1]} \n{place[2]}")
print("Where should the rabbit go? 🐇")

Chioce= input("Please enter a row and acolumn: ")
row= int(Chioce[0])
column= int(Chioce[1])
place[row-1][column-1]= "🐇"

print("\n success ....\n")
print(f"{place[0]} \n{place[1]}\n{place[2]}")