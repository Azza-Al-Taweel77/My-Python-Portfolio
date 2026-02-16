import string
sentence= input("Please type a sentence: ")
new_sentence= ""
for M in sentence:
    if M not in string.punctuation:
        new_sentence += M
print("*** Here is the same sentence without punctuation ***")
print(new_sentence)