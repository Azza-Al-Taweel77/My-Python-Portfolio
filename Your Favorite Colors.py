Your_Color= input("Add the first color you like: ")
colors= []
colors.append(Your_Color)
Next= input("Do you wand to add more colors? Yes, or No?")

if Next.lower() == "yes":
    More= input("Add anther color to the list:")
    colors.append(More)
    print(f"The colors you like are: {colors}")
else:
    print(f"The colors you like are: {colors}")