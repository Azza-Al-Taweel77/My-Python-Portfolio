Books=[]
Your_Books= input("Enter the name of a book you own: ").lower()
Next= input("Enter the name of another book you own (or press 'Enter' to skip): ").lower()
 
if Next:
    Books.append(Your_Books)
    Books.append(Next)
    print(f"Your Library: {Books}")
else:
    Books.append(Your_Books)
    print(f"Your Library: {Books}")
Future= []
Future_books= input("Enter the name of a book you wish to have in the future: ").lower()
Future_Next= input("Enter the name of another book you wish to have (or press 'Enter' to skip): ").lower()

if Future_Next:
    Future.append(Future_books)
    Future.append(Future_Next)
    print(f"Your Wishlist: {Future}")
else:
    Future.append(Future_books)
    print(f"Your Wishlist: {Future}")

New_Own= input("Enter the name of a book from your Wishlist that you,ve quired (or ress 'Enter' to skip): ").lower()
if New_Own:
    Future.remove(New_Own)
    Books.append(New_Own)
    print(f"Updated Library: {Books}")
    print(f"Updated Wishlist: {Future}")
donate= input("Enter the name of a book from your library you wish to donate (or press 'Enter' yo skip): ")
if donate:
    Books.remove(donate)
    print(f"Final Library after Donations: {Books}")
else:
    print(f"Final Library : {Books}")